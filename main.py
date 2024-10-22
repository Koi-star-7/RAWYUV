# This Python file uses the following encoding: utf-8
import sys
import os.path

from yuv_to_rgb import *
from raw_to_rgb import *
from ImageView import ImageView

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QImage, QPixmap, QPen, QColor
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QDialog, QGraphicsScene, QGraphicsPixmapItem, \
    QMessageBox, QGraphicsView, QGraphicsLineItem, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, \
    QPushButton, QGraphicsTextItem, QTableWidget, QTableWidgetItem, QSizePolicy, QInputDialog

from ui_form import Ui_Widget
from ui_config import Ui_Dialog
from ui_raw_info import Ui_Raw_info
from ui_yuv_info import Ui_yuv_info
from ui_file_raw import Ui_file_save
from ui_yuv_config import Ui_YUV_Config
from ui_save_raw import Ui_save_raw_Form
from ui_save_yuv import Ui_save_yuv_Form
from ui_compare import Ui_Compare

# 显示和修改RAW图像的参数
class RAW_INFO(QWidget):
    # 定义一个信号，用于通知外部需要清除的像素数据
    clear_pix = Signal()

    def __init__(self, parent=None, parameters=None, file_path=None):
        super().__init__(parent)  # 调用父类的构造函数
        self.file_path = file_path  # 存储文件路径
        self.parameters = parameters  # 存储参数
        self.info = Ui_Raw_info()  # 创建用户界面实例
        self.info.setupUi(self)  # 设置窗口的用户界面
        self.pattern = self.parameters['bayer_pattern']  # 获取Bayer模式参数
        self.info.height.setText(str(self.parameters['height']))  # 在界面上显示图像的高度信息
        self.info.width.setText(str(self.parameters['width']))  # 在界面上显示图像的宽度信息
        self.info.bit_depth.setText(str(self.parameters['bit_depth']))  # 在界面上显示图像的位深度信息
        self.set_bayer_pattern()  # 设置Bayer模式
        self.info.checkBox.setChecked(self.parameters['big_endian'])  # 根据参数设置复选框状态
        self.info.reload.clicked.connect(self.reload_signal)  # 当点击“reload”按钮时，连接到相应的槽函数
        self.info.Demosica.setChecked(True)  # 设置Demosica模式为默认选中状态

    # 根据当前的拜耳模式设置界面上的单选按钮状态
    def set_bayer_pattern(self):
        if self.pattern == 'RGGB':
            self.info.rg.setChecked(True)
        elif self.pattern == 'BGGR':
            self.info.bg.setChecked(True)
        elif self.pattern == 'GBRG':
            self.info.gb.setChecked(True)
        elif self.pattern == 'GRBG':
            self.info.gr.setChecked(True)

    # 获取当前选中的拜耳模式
    def get_bayer_pattern(self):
        if self.info.rg.isChecked():
            return 'RGGB'
        elif self.info.bg.isChecked():
            return 'BGGR'
        elif self.info.gr.isChecked():
            return 'GRBG'
        elif self.info.gb.isChecked():
            return 'GBRG'

    # 获取颜色校正矩阵（CCM）的数据
    def get_ccm_data(self):
        data = np.zeros((3, 3))
        for row in range(3):
            for col in range(3):
                item = self.info.model.item(row, col)
                try:
                    # 将界面上的文本转换为浮点数，如果转换失败则设置为 0.0
                    data[row, col] = float(item.text())
                except ValueError:
                    data[row, col] = 0.0
        return data

    # 当点击“重新加载”按钮时调用的槽函数
    def reload_signal(self):
        # 更新参数中的拜耳模式
        self.parameters['bayer_pattern'] = self.get_bayer_pattern()

        # 更新参数中的调整标志
        self.parameters['adjust'] = self.info.groupBox_3.isChecked()
        if self.parameters['adjust']:
            # 更新参数中的白平衡设置、伽马值和颜色校正矩阵相关的参数
            self.parameters['wb'] = self.info.wb.currentText()
            self.parameters['gamma'] = self.info.gamma.text()
            self.parameters['ccm_checked'] = self.info.groupBox_2.isChecked()
            self.parameters['view_mode'] = self.get_view_mode()
            if self.parameters['ccm_checked']:
                self.parameters['ccm'] = self.get_ccm_data()

        # 发射清除像素数据的信号
        self.clear_pix.emit()

    def get_view_mode(self):
        if self.info.Demosica.isChecked():
            return 'Demosica'
        elif self.info.Bayer.isChecked():
            return 'Bayer'
        return 'Demosica'

# 显示和修改YUV图像的参数信息
class YUV_INFO(QWidget):
    # 定义一个信号，用于通知外部需要清除像素数据
    clear_pix = Signal()

    def __init__(self, parent=None, parameters=None, file_path=None):
        super().__init__(parent)  # 调用父类的构造函数
        self.file_path = file_path  # 存储文件路径
        self.parameters = parameters  # 存储参数
        self.info = Ui_yuv_info()  # 创建用户界面示例
        self.info.setupUi(self)  # 设置窗口的用户界面
        self.info.height.setText(str(self.parameters['height']))  # 在界面上显示图像的高度信息
        self.info.width.setText(str(self.parameters['width']))  # 在界面上显示图像的宽度信息
        self.info.pattern.setText(self.parameters['yuv_pattern'])  # 在界面上显示YUV格式信息
        self.info.checkBox.setChecked(self.parameters['TV_range'])  # 根据参数设置复选框的状态
        self.info.comboBox_3.setCurrentText(self.parameters['standard'])  # 设置下拉框的当前文本位参数中的标准
        self.info.Y_channel.setChecked(True)  # 默认选中Y、Cr、Cb通道的复选框
        self.info.Cr_channel.setChecked(True)
        self.info.Cb_channel.setChecked(True)
        self.info.reload.clicked.connect(self.reload_signal)  # 当点击“reload”按钮时，连接到相应的槽函数
        self.info.Y_channel.stateChanged.connect(self.check_selection)  # 当Y、Cr、Cb通道的复选框状态改变时，连接到相应的槽函数
        self.info.Cr_channel.stateChanged.connect(self.check_selection)
        self.info.Cb_channel.stateChanged.connect(self.check_selection)

    # 当点击“重新加载”按钮时调用的槽函数
    def reload_signal(self):
        # 更新参数中的标准、TV 范围标志、插值方法以及 Y、Cr、Cb 通道的选中状态
        self.parameters['standard'] = self.info.comboBox_3.currentText()
        self.parameters['TV_range'] = self.info.checkBox.isChecked()
        self.parameters['interpolation'] = self.info.comboBox.currentText()
        self.parameters['Y'] = self.info.Y_channel.isChecked()
        self.parameters['Cr'] = self.info.Cr_channel.isChecked()
        self.parameters['Cb'] = self.info.Cb_channel.isChecked()

        # 发射清除像素数据的信号
        self.clear_pix.emit()

    # 当 Y、Cr、Cb 通道的复选框状态改变时调用的槽函数
    def check_selection(self):
        # 如果 Y、Cr、Cb 通道都没有被选中，显示警告框
        if not (self.info.Y_channel.isChecked() or self.info.Cr_channel.isChecked() or
                self.info.Cb_channel.isChecked()):
            QMessageBox.warning(self, "Selection", "You must select at least one option.")

# 从指定路径中读取原始数据并进行处理的函数
def process_raw_file(file_path, params):
    # 创建一个 RawImage 实例，传入文件路径和参数
    raw_image = RawImage(
        file_path=file_path,
        parameters=params)

    # 调用 RawImage 实例的 read_data 方法读取数据
    raw_image.read_data()

    # 返回读取到的数据
    return raw_image.data

# 配置图像参数的对话框
class ImageConfigDialog(QDialog):
    def __init__(self, parent=None, is_raw=True):
        super().__init__(parent)  # 调用父类的构造函数
        self.config = Ui_Dialog() if is_raw else Ui_YUV_Config()  # 根据是否为原始数据选择不同的 UI 文件
        self.config.setupUi(self)  # 设施对话框的用户界面
        self.is_raw = is_raw  # 标记是否位raw图像
        self.parameters = {}  # 存储参数的字典

        # 如果不是raw图像，设置相关下拉框选项和信号连接
        if not is_raw:
            self.config.comboBox.addItems(['4:4:4', '4:2:2', '4:2:0'])
            self.config.comboBox.currentTextChanged.connect(self.update_item)

    # 当对话框被接受时（用户点击确认按钮）的处理办法
    def accept(self):
        # 如果是raw图像，设置raw图像的参数
        if self.is_raw:
            self.parameters = {
                'height': int(self.config.height.text()),
                'width': int(self.config.height_2.text()),
                'bit_depth': int(self.config.comboBox.currentText()),
                'bayer_pattern': self.get_bayer_pattern(),
                'big_endian': self.config.checkBox.isChecked(),
                'compression': self.config.checkBox_2.isChecked(),
                'adjust': False
            }
        else:
            # 如果不是raw图像，设置yuv图像的参数
            self.parameters = {
                'height': int(self.config.height.text()),
                'width': int(self.config.width.text()),
                'yuv_pattern': self.config.comboBox_2.currentText(),
                'standard': self.config.comboBox_3.currentText(),
                'TV_range': self.config.checkBox.isChecked(),
                'Y': True,
                'Cr': True,
                'Cb': True,
                'interpolation': 'nearest'
            }

        # 调用父类的accept方法，关闭对话框并发出接受信号
        super().accept()

    # 获取bayer模式的方法
    def get_bayer_pattern(self):
        if self.config.rg.isChecked():
            return 'RG'
        elif self.config.bg.isChecked():
            return 'BG'
        elif self.config.gr.isChecked():
            return 'GR'
        elif self.config.gb.isChecked():
            return 'GB'

    # 当下拉框文本改变时的处理方法，用于更新yuv格式的下拉框选项
    def update_item(self, text):
        self.config.comboBox_2.clear()
        if text == '4:4:4':
            self.config.comboBox_2.addItems(['I444', 'NV24', 'NV42', 'AYUV'])
        elif text == '4:2:2':
            self.config.comboBox_2.addItems(['I422', 'NV16', 'NV61', 'YUYV', 'UYVY'])
        elif text == '4:2:0':
            self.config.comboBox_2.addItems(['I420', 'YV21', 'NV12', 'NV21'])

# 图像保存对话框类，用于让用户选择要保存的图像文件的格式、路径和文件名等
class ImageSaveDialog(QDialog):
    # 定义一个信号，用于传递保存图像的参数
    recv_format = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类的初始化方法
        self.file_ext = None  # 存储文件扩展名
        self.file_path = None  # 存储文件路径
        self.save_file = None  # 存储要保存的文件对象（如果有）
        self.parameters = {  # 存储保存图像的参数的字典
            'type': '',
            'path': '',
            'name': '',
            'special': False,
            'pattern': '',
            'pattern2': ''
        }
        self.file_save = Ui_file_save()  # 创建用户界面实例
        self.file_save.setupUi(self)  # 设置对话框的用户界面
        print('hello')  # 打印调试信息
        self.file_save.filepath_choose.clicked.connect(self.update_filepath)  # 当点击“选择路径”按钮时，连接到相应的槽函数

    # 当对话框被接受时（用户点击确定按钮）的处理方法
    def accept(self):
        self.file_ext = self.file_save.type.currentText()
        if self.file_ext == '.raw':
            # 如果保存的文件拓展名为 .raw，设置特殊标志为True
            self.parameters['special'] = True

            # # 创建 ImageSaveFormatDialog 实例，并传入当前对象和默认参数 True
            self.save_file = ImageSaveFormatDialog(self)

            # 将对话框的 save_format 信号连接到当前对象的 receiver_format 槽函数
            self.save_file.save_format.connect(self.receiver_format)

            # 执行对话框，显示并等待用户交互
            self.save_file.exec()
        elif self.file_ext == '.yuv':
            # 如果文件扩展名为.yuv，设置特殊标志为 True
            self.parameters['special'] = True

            # 创建 ImageSaveFormatDialog 实例，并传入当前对象和参数 False
            self.save_file = ImageSaveFormatDialog(self, False)

            # 将对话框的 save_format 信号连接到当前对象的 receiver_format 槽函数
            self.save_file.save_format.connect(self.receiver_format)

            # 执行对话框，显示并等待用户交互
            self.save_file.exec()
        else:
            # 如果不是特殊格式，设置特殊标志为 False
            self.parameters['special'] = False

            # 设置非特殊格式下的参数，包括文件名、文件路径和文件类型
            self.parameters['name'] = self.file_save.filename.text()
            self.parameters['path'] = self.file_save.fiepath.text()
            self.parameters['type'] = self.file_ext

            # 打印非特殊格式下的最终参数
            print(f"Final parameters for non-special format: {self.parameters}")

            # 发射信号，传递非特殊格式的参数
            self.recv_format.emit(self.parameters)

        # 调用父类的 accept 方法
        super().accept()

    # 设置文件路径和文件名的方法
    def set_file_path_name(self, path, name, file_type):
        print(path, name, file_type)
        self.file_save.fiepath.setText(path)  # 在界面上设置文件路径
        self.file_save.filename.setText(name)  # 在界面上设置文件名
        self.file_save.type.setCurrentText(file_type)  # 在界面上设置文件类型

    # 当点击“选择路径”按钮时调用的槽函数，用于更新文件路径
    def update_filepath(self):
        filepath = QFileDialog.getExistingDirectory(self, "选择目录", "")
        if filepath:
            self.parameters['path'] = filepath

            # 更新界面上的文件路径显示
            self.file_save.fiepath.setText(filepath)

    # 接收格式的槽函数，用于处理从保存格式对话框中传来的格式信息
    def receiver_format(self, text1, text2):
        # 设置保存图像的参数中的格式信息
        self.parameters['pattern'] = text1
        self.parameters['pattern2'] = text2
        self.parameters['name'] = self.file_save.filename.text()  # 获取用户输入的文件名
        self.parameters['path'] = self.file_save.fiepath.text()  # 获取用户选择的文件路径
        self.parameters['type'] = self.file_ext  # 获取文件扩展名
        print(self.parameters)  # 打印参数信息
        self.recv_format.emit(self.parameters)  # 发射信号，传递保存图像的参数

# 用户选择图像保存格式的对话框类
class ImageSaveFormatDialog(QDialog):
    # 定义一个信号，用于传递保存格式信息
    save_format = Signal(str, str)

    def __init__(self, parent=None, is_raw=True):
        super().__init__(parent)  # 调用父类的初始化方法
        self.is_raw = is_raw  # 标记是否为raw图像格式

        # 如果是raw图像格式
        if is_raw:
            self.file_save = Ui_save_raw_Form()  # 创建raw图像保存格式的用户界面实例
            print(self.file_save.__module__)  # 打印用户界面模块信息，用于调试
            self.file_save.setupUi(self)  # 设置用户界面
            self.file_save.compress.clicked.connect(self.comboBox_ok)  # 当“压缩”复选框被点击时，连接到相应的槽函数
        else:
            # 如果不是raw图像格式，创建 YUV 图像保存格式的用户界面实例
            self.file_save = Ui_save_yuv_Form()
            self.file_save.setupUi(self)  # 设置用户界面
            self.file_save.head.currentTextChanged.connect(self.update_item)  # 当下拉框“头部信息”的文本改变时，连接到相应的槽函数
        print(is_raw)  # 打印是否为raw图像格式的信息，用于调试
        self.file_save.pushButton.clicked.connect(self.accept)  # 当点击“确定”按钮时，连接到相应的槽函数

    # 当对话框被接受时（用户点击确定按钮）的处理方法
    def accept(self):
        # 如果是raw图像格式，调用获取raw图像格式的方法
        if self.is_raw:
            self.get_raw_format()
        else:
            self.get_yuv_format()  # 如果不是raw图像格式，调用获取 YUV 图像格式的方法

    # 当“压缩”复选框被点击时的槽函数
    def comboBox_ok(self):
        # 根据“压缩”复选框的状态，设置“压缩位数”下拉框是否可用
        self.file_save.bit.setEnabled(self.file_save.compress.isChecked())

    # 当下拉框“头部信息”的文本改变时的槽函数，用于更新 YUV 格式的下拉框选项
    def update_item(self, text):
        self.file_save.format.clear()
        if text == '4:4:4':
            self.file_save.format.addItems(['I444', 'NV24', 'NV42', 'AYUV'])
        elif text == '4:2:2':
            self.file_save.format.addItems(['I422', 'NV16', 'NV61', 'YUYV', 'UYVY'])
        elif text == '4:2:0':
            self.file_save.format.addItems(['I420', 'YV12', 'YV21', 'NV12', 'NV21'])

    # 获取原始图像保存格式的方法
    def get_raw_format(self):
        # 获取拜耳模式
        bayer_pattern = self.file_save.bayer.currentText()

        # 判断是否选择了压缩
        is_compress = self.file_save.compress.isChecked()

        if is_compress:
            # 如果选择了压缩，获取压缩位数，并发射信号传递拜耳模式和压缩位数
            compress_bit = self.file_save.bit.currentText()
            self.save_format.emit(bayer_pattern, compress_bit)
        else:
            # 如果没有选择压缩，发射信号传递拜耳模式和空字符串
            self.save_format.emit(bayer_pattern, "")

    # 获取 YUV 图像保存格式的方法
    def get_yuv_format(self):
        # 获取头部信息
        head = self.file_save.head.currentText()

        # 获取 YUV 格式
        yuv_format = self.file_save.format.currentText()

        # 获取标准
        standard = self.file_save.standard.currentText()

        # 获取是否为 TV 类型的标志
        tv_type = self.file_save.TV_type.isChecked()

        # 将 YUV 格式信息封装为字典
        yuv_format = {
            'format': yuv_format,
            'standard': standard,
            'tv_type': tv_type
        }

        # 发射信号，传递头部信息和 YUV 格式字典
        self.save_format.emit(head, str(yuv_format))

class Widget(QWidget):
    # 类的初始化方法
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类的初始化方法
        self.compare_ui = Ui_Compare()  # 初始化比较界面
        self.save_file = None  # 保存文件的变量，初始为空
        self.pattern2 = None  # 第二个模式的变量，初始为空
        self.pattern = None  # 模式的变量，初始为空
        self.file_save_path = None  # 文件保存路径的变量，初始为空
        self.file_ext = None  # 文件扩展名的变量，初始为空
        self.data = None  # 数据的变量，初始为空
        self.ui = Ui_Widget()  # 初始化界面
        self.ui.setupUi(self)  # 设置界面
        # 连接按钮的点击事件到对应的方法
        self.ui.RawC.clicked.connect(self.choose_raw)
        self.ui.YuvC.clicked.connect(self.choose_yuv)
        self.ui.convert.clicked.connect(self.convert)
        self.ui.one_to_one.clicked.connect(self.one_to_one)
        self.ui.gridline.clicked.connect(self.gridline)
        self.ui.compare.clicked.connect(self.compare)
        self.info = None  # 信息的变量，初始为空
        self.scene = None  # 场景的变量，初始为空
        self.parameters = None  # 参数的变量，初始为空
        self.file_path = None  # 文件路径的变量，初始为空
        self.is_raw = True  # 是否为原始图像的标志，初始为True
        self.image_view = ImageView()  # 初始化图像视图
        self.ui.showView.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)  # 设置视图更新模式
        self.has_image_displayed = False  # 标记是否有图像显示，初始为False
        self.setMouseTracking(True)  # 开启鼠标追踪
        self.compare_window = None  # 比较窗口的变量，初始为空

    def resizeEvent(self, event):
        # 当窗口大小改变时，调整图像视图的大小
        new_size = event.size()  # 获取新窗口大小
        old_size = event.oldSize()  # 获取旧窗口大小
        width_diff = new_size.width() - old_size.width()  # 计算宽度变化
        height_diff = new_size.height() - old_size.height()  # 计算高度变化
        transform = self.image_view.transform()  # 获取图像视图的当前变换
        scale_x = transform.m11()  # 获取水平缩放比例
        scale_y = transform.m22()  # 获取垂直缩放比例
        self.image_view.resetTransform()  # 重置图像视图的变换
        self.image_view.scale(scale_x, scale_y)  # 应用之前的缩放比例
        if self.image_view.scene():  # 如果有场景
            scene_rect = self.image_view.scene().sceneRect()  # 获取场景矩形
            view_rect = self.image_view.viewport().rect()  # 获取视图矩形
            view_center_x = view_rect.center().x()  # 获取视图中心的x坐标
            view_center_y = view_rect.center().y()  # 获取视图中心的y坐标
            scene_center_x = scene_rect.center().x()  # 获取场景中心的x坐标
            scene_center_y = scene_rect.center().y()  # 获取场景中心的y坐标
            new_translate_x = transform.dx() + width_diff / 2 - (view_center_x - scene_center_x)  # 计算新的水平平移量
            new_translate_y = transform.dy() + height_diff / 2 - (view_center_y - scene_center_y)  # 计算新的垂直平移量
            self.image_view.translate(new_translate_x, new_translate_y)  # 应用新的平移量

    def choose_raw(self):
        # 选择原始图像文件
        file_dialog = QFileDialog(self, "选择 Raw 图", "", "图片类型(*.raw)")  # 创建文件对话框
        if file_dialog.exec():  # 如果用户选择了文件
            self.file_path = file_dialog.selectedFiles()[0]  # 获取文件路径
            self.ui.RawPath.setText(self.file_path)  # 在界面上显示文件路径
            self.show_config_dialog(is_raw=True)  # 显示配置对话框

    def choose_yuv(self):
        # 选择YUV图像文件
        file_dialog = QFileDialog(self, "选择 yuv 图", "", "图片类型(*.yuv)")  # 创建文件对话框
        if file_dialog.exec():  # 如果用户选择了文件
            self.file_path = file_dialog.selectedFiles()[0]  # 获取文件路径
            self.ui.YuvPath.setText(self.file_path)  # 在界面上显示文件路径
            self.show_config_dialog(is_raw=False)  # 显示配置对话框

    def convert(self):
        # 转换图像格式
        self.save_file = ImageSaveDialog(self)  # 创建保存对话框
        path, name = os.path.split(self.file_path)  # 分割文件路径和文件名
        name, self.file_ext = os.path.splitext(name)  # 分割文件名和扩展名
        self.save_file.set_file_path_name(path, name, self.file_ext)  # 设置保存对话框的路径和文件名
        self.save_file.recv_format.connect(self.save_path)  # 连接信号
        self.save_file.exec()  # 执行保存对话框

    def one_to_one(self):
        # 将图像视图缩放到1:1的比例
        self.image_view.resetTransform()  # 重置图像视图的变换
        self.image_view.scale(1, 1)  # 将图像缩放到1:1的比例

    def gridline(self):
        # 如果已经存在网格线对话框并且是可见的，则关闭它
        if hasattr(self, 'gridline_dialog') and self.gridline_dialog.isVisible():
            self.gridline_dialog.reject()
        # 创建新的网格线设置对话框
        self.gridline_dialog = QDialog(self)
        self.gridline_dialog.setWindowTitle("设置网格线数量")
        layout = QVBoxLayout()
        # 创建水平网格线数量的标签和输入框
        horizontal_label = QLabel("横向网格线数量：")
        self.horizontal_input = QLineEdit()
        layout.addWidget(horizontal_label)
        layout.addWidget(self.horizontal_input)
        # 创建垂直网格线数量的标签和输入框
        vertical_label = QLabel("纵向网格线数量：")
        self.vertical_input = QLineEdit()
        layout.addWidget(vertical_label)
        layout.addWidget(self.vertical_input)
        # 创建按钮布局
        button_layout = QHBoxLayout()
        ok_button = QPushButton("确定")
        ok_button.clicked.connect(self.handle_ok_button_with_update_gridlines)
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.gridline_dialog.reject)
        clear_button = QPushButton("清除网格线")
        clear_button.clicked.connect(self.clear_gridlines)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(clear_button)
        layout.addLayout(button_layout)
        # 设置对话框的布局，并显示对话框
        self.gridline_dialog.setLayout(layout)
        self.gridline_dialog.show()

    def handle_ok_button_with_update_gridlines(self):
        # 当点击确定按钮时，更新网格线并关闭对话框
        self.update_gridlines()
        self.gridline_dialog.close()

    def update_gridlines(self):
        # 更新网格线
        horizontal_count = int(self.horizontal_input.text())  # 获取水平网格线数量
        vertical_count = int(self.vertical_input.text())  # 获取垂直网格线数量
        pen = QPen(QColor(255, 0, 0), 1)  # 设置网格线颜色和宽度
        scene_rect = self.scene.sceneRect()  # 获取场景矩形
        width = scene_rect.width()
        height = scene_rect.height()
        # 移除现有的网格线和文本项
        for item in self.scene.items():
            if isinstance(item, QGraphicsLineItem) or isinstance(item, QGraphicsTextItem):
                self.scene.removeItem(item)
        # 绘制新的网格线
        for i in range(horizontal_count):
            line_item = QGraphicsLineItem(0, i * height / horizontal_count, width, i * height / horizontal_count)
            line_item.setPen(pen)
            self.scene.addItem(line_item)
        for i in range(vertical_count):
            line_item = QGraphicsLineItem(i * width / vertical_count, 0, i * width / vertical_count, height)
            line_item.setPen(pen)
            self.scene.addItem(line_item)
        # 创建数字输入对话框
        self.table_dialog = self.create_table_dialog()

    def create_table_dialog(self):
        # 创建数字输入对话框
        table_dialog = QDialog(self)
        table_dialog.setWindowTitle("输入对应网格中的数字")
        horizontal_count = int(self.horizontal_input.text())  # 获取水平网格线数量
        vertical_count = int(self.vertical_input.text())  # 获取垂直网格线数量
        table_widget = QTableWidget(horizontal_count, vertical_count)
        table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        input_widgets = [[None] * vertical_count for _ in range(horizontal_count)]
        # 初始化表格项
        for row in range(horizontal_count):
            for col in range(vertical_count):
                input_widgets[row][col] = QTableWidgetItem()
                table_widget.setItem(row, col, input_widgets[row][col])
                input_widgets[row][col].setFlags(
                    input_widgets[row][col].flags() | Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(row, col, input_widgets[row][col])
        # 创建按钮并连接信号
        ok_button_table = QPushButton("确定")
        ok_button_table.clicked.connect(lambda: self.draw_numbers(input_widgets))
        import_button = QPushButton("导入")
        import_button.clicked.connect(lambda: self.import_numbers(input_widgets))
        export_button = QPushButton("导出")
        export_button.clicked.connect(lambda: self.export_numbers(input_widgets))
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button_table)
        button_layout.addWidget(import_button)
        button_layout.addWidget(export_button)
        table_layout = QVBoxLayout()
        table_layout.addWidget(table_widget)
        table_layout.addLayout(button_layout)
        table_dialog.setLayout(table_layout)
        table_dialog.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        table_dialog.resize(500, 300)
        table_dialog.show()
        return table_dialog

    def handle_double_click(self, event):
        # 处理双击事件，允许编辑网格中的数字
        item = self.scene.itemAt(event.scenePos(), self.image_view.transform())
        if isinstance(item, QGraphicsTextItem):
            current_text = item.toPlainText()
            new_text, ok = QInputDialog.getText(self, "编辑数字", "输入新数字：", text=current_text)
            if ok:
                item.setPlainText(new_text)
                # 更新表格中的数字
                scene_rect = self.scene.sceneRect()
                width = scene_rect.width()
                height = scene_rect.height()
                horizontal_count = int(self.horizontal_input.text())
                vertical_count = int(self.vertical_input.text())
                x = item.pos().x()
                y = item.pos().y()
                col = int(x * vertical_count / width)
                row = int(y * horizontal_count / height)
                existing_table_dialog = self.table_dialog
                if existing_table_dialog:
                    table_widget = existing_table_dialog.findChild(QTableWidget)
                    if table_widget:
                        existing_item = table_widget.item(row, col)
                        if existing_item:
                            existing_item.setText(new_text)
                # 重新定位文本项
                new_x = col * width / vertical_count + width / vertical_count / 2
                new_y = row * height / horizontal_count + height / horizontal_count / 2
                item.setPos(new_x - item.boundingRect().width() / 2, new_y - item.boundingRect().height() / 2)
                # 移除重复的文本项
                for old_item in [i for i in self.scene.items() if isinstance(i, QGraphicsTextItem)]:
                    if old_item.pos().x() == x - old_item.boundingRect().width() / 2 and old_item.pos().y() == y - old_item.boundingRect().height() / 2 and old_item.toPlainText() != new_text:
                        self.scene.removeItem(old_item)

    def draw_numbers(self, input_widgets):
        # 在网格中绘制数字
        horizontal_count = int(self.horizontal_input.text())
        vertical_count = int(self.vertical_input.text())
        scene_rect = self.scene.sceneRect()
        width = scene_rect.width()
        height = scene_rect.height()
        existing_text_items = [item for item in self.scene.items() if isinstance(item, QGraphicsTextItem)]
        for row in range(horizontal_count):
            for col in range(vertical_count):
                number = input_widgets[row][col].text()
                if number:
                    x = col * width / vertical_count + width / vertical_count / 2
                    y = row * height / horizontal_count + height / horizontal_count / 2
                    existing_item = None
                    for item in existing_text_items:
                        if item.pos().x() == x - item.boundingRect().width() / 2 and item.pos().y() == y - item.boundingRect().height() / 2:
                            existing_item = item
                            break
                    if existing_item:
                        existing_item.setPlainText(number)
                    else:
                        text_item = QGraphicsTextItem(number)
                        font = text_item.font()
                        font.setPointSize(min(width / vertical_count, height / horizontal_count) // 2)
                        text_item.setFont(font)
                        text_item.setDefaultTextColor(QColor(255, 255, 255))
                        text_item.setOpacity(0.7)
                        text_item.setPos(x - text_item.boundingRect().width() / 2,
                                         y - text_item.boundingRect().height() / 2)
                        text_item.setAcceptedMouseButtons(Qt.LeftButton)
                        text_item.mouseDoubleClickEvent = lambda event: self.handle_double_click(event)
                        self.scene.addItem(text_item)

    def clear_gridlines(self):
        # 清除网格线和文本项
        for item in self.scene.items():
            if isinstance(item, QGraphicsLineItem) or isinstance(item, QGraphicsTextItem):
                self.scene.removeItem(item)

    def import_numbers(self, input_widgets):
        # 从文本文件导入数字到表格中
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件", "", "文本文件 (*.txt)")  # 打开文件选择对话框
        if file_path:  # 如果选择了文件
            with open(file_path, 'r', encoding='utf-8') as file:  # 读取文件内容
                content = file.read()
                numbers = [part.strip() for part in content.split(',') if part.strip()]  # 分割文件内容并去除空白
                horizontal_count = int(self.horizontal_input.text())  # 获取水平网格线数量
                vertical_count = int(self.vertical_input.text())  # 获取垂直网格线数量
                total_cells = horizontal_count * vertical_count  # 计算总单元格数量
                if len(numbers) != total_cells:  # 如果文件中的数字数量与网格线数量不匹配
                    QMessageBox.warning(self, "错误", "所选文件数据数量错误")  # 显示警告消息
                    return
                index = 0
                for row in range(horizontal_count):  # 遍历每一行
                    for col in range(vertical_count):  # 遍历每一列
                        if index < len(numbers):  # 如果索引在范围内
                            input_widgets[row][col].setText(numbers[index])  # 将数字设置到表格项中
                            index += 1  # 增加索引

    def export_numbers(self, input_widgets):
        # 将表格中的数字导出到文本文件
        horizontal_count = int(self.horizontal_input.text())  # 获取水平网格线数量
        vertical_count = int(self.vertical_input.text())  # 获取垂直网格线数量
        has_empty = False  # 标记是否有空缺的单元格
        for row in range(horizontal_count):  # 遍历每一行
            for col in range(vertical_count):  # 遍历每一列
                item = input_widgets[row][col]  # 获取表格项
                if item is None or item.text() == "":  # 如果表格项为空
                    has_empty = True  # 设置有空缺的标记
                    break  # 跳出循环
            if has_empty:  # 如果有空缺的单元格
                break  # 跳出循环
        if has_empty:  # 如果有空缺的单元格
            QMessageBox.warning(self, "错误", "表格有空缺")  # 显示警告消息
            return  # 返回
        content = ""  # 初始化内容字符串
        for row in range(horizontal_count):  # 遍历每一行
            for col in range(vertical_count):  # 遍历每一列
                item = input_widgets[row][col]  # 获取表格项
                if item is not None:  # 如果表格项不为空
                    content += item.text()  # 将表格项的文本添加到内容字符串
                if col < vertical_count - 1:  # 如果不是最后一列
                    content += ","  # 添加逗号分隔符
            content += "\n"  # 每行结束后添加换行符
        file_dialog = QFileDialog()  # 创建文件对话框
        file_path, _ = file_dialog.getSaveFileName(self, "保存文件", "", "文本文件 (*.txt)")  # 打开保存文件对话框
        if file_path:  # 如果选择了文件路径
            with open(file_path, 'w', encoding='utf-8') as file:  # 写入文件
                file.write(content)  # 写入内容字符串

    def get_table_item(self, row, col):
        # 获取表格项
        input_widgets = [[None] * int(self.vertical_input.text()) for _ in
                         range(int(self.horizontal_input.text()))]  # 创建表格项列表
        return input_widgets[row][col] if input_widgets[row][col] is not None else None  # 返回表格项，如果为空则返回None

    def dragEnterEvent(self, event):
        # 当拖拽事件进入窗口时，检查是否有URLs数据
        if event.mimeData().hasUrls():
            event.acceptProposedAction()  # 如果有，接受拖放动作

    def dropEvent(self, event):
        # 当释放拖放事件时，处理拖放的文件
        for url in event.mimeData().urls():  # 遍历所有拖放的URLs
            file_path = url.toLocalFile()  # 将URL转换为本地文件路径
            if self.has_image_displayed:  # 如果已经显示了图像
                reply = QMessageBox.question(self, "替换图像", "场景中已有图像，是否替换？",
                                             QMessageBox.Yes | QMessageBox.No)  # 询问用户是否替换
                if reply == QMessageBox.No:  # 如果用户选择不替换
                    continue  # 跳过当前文件
                self.scene.clear()  # 清除当前场景
                self.has_image_displayed = False  # 重置图像显示标记
            # 根据文件扩展名处理不同类型的图像文件
            if file_path.endswith('.raw'):
                self.file_path = file_path  # 设置文件路径
                self.ui.RawPath.setText(self.file_path)  # 在界面上显示文件路径
                self.show_config_dialog(is_raw=True)  # 显示配置对话框，表明是原始图像
            elif file_path.endswith('.yuv'):
                self.file_path = file_path  # 设置文件路径
                self.ui.YuvPath.setText(self.file_path)  # 在界面上显示文件路径
                self.show_config_dialog(is_raw=False)  # 显示配置对话框，表明不是原始图像
            elif file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.bmp'):
                self.show_RGB(file_path)  # 显示RGB图像

    def compare(self):
        self.compare_window = QDialog(self)
        self.compare_ui.setupUi(self.compare_window)
        self.compare_window.show()

    def save_path(self, pattern):
        # 保存图像到指定路径和格式
        self.file_ext = pattern['type']  # 获取文件扩展名
        self.file_save_path = pattern['path'] + '/' + pattern['name'] + pattern['type']  # 构造文件保存路径
        if pattern['special']:  # 如果有特殊配置
            self.pattern = pattern['pattern']  # 设置第一模式
            self.pattern2 = pattern['pattern2']  # 设置第二模式
        # 根据文件扩展名处理不同类型的图像文件保存
        if self.file_ext == '.raw':
            if not self.pattern2:
                data = rgb2raw(self.data, 16, self.pattern)  # 转换RGB数据到RAW格式
                cv2.imwrite(self.file_save_path, data, (data.shape[1], data.shape[0]))  # 保存RAW图像
            else:
                data = rgb2raw(self.data, self.pattern2, self.pattern, True)  # 转换RGB数据到RAW格式
                cv2.imwrite(self.file_save_path, data, (data.shape[1], data.shape[0]))  # 保存RAW图像
        elif self.file_ext == '.yuv':
            self.pattern2 = eval(self.pattern2)  # 评估第二模式
            yuv_data = rgb2yuv(self.data, self.pattern, self.pattern2['format'], self.pattern2['standard'],
                               self.pattern2['tv_type'])  # 转换RGB数据到YUV格式
            # 根据YUV格式重新整形数据
            if self.pattern == '4:4:4':
                reshaped_data = yuv_data.reshape((self.parameters['height'], self.parameters['width']))
            elif self.pattern == '4:2:2':
                reshaped_data = yuv_data.reshape((self.parameters['height'] * 2, self.parameters['width']))
            elif self.pattern == '4:2:0':
                reshaped_data = yuv_data.reshape((self.parameters['height'] * 3 // 2, self.parameters['width']))
            with open(self.file_save_path, 'wb') as f:  # 保存YUV图像
                f.write(reshaped_data)
        else:
            img = cv2.cvtColor(self.data, cv2.COLOR_RGB2BGR)  # 转换RGB数据到BGR格式
            cv2.imwrite(self.file_save_path, img)  # 保存BGR图像
        self.save_file.close()  # 关闭保存对话框

    def show_config_dialog(self, is_raw):
        # 显示图像配置对话框
        config_dialog = ImageConfigDialog(self, is_raw)  # 创建配置对话框
        if config_dialog.exec() == QDialog.Accepted:  # 如果用户接受了配置
            self.parameters = config_dialog.parameters  # 获取配置参数
            self.is_raw = is_raw  # 设置是否为原始图像
            self.image_choose()  # 选择并显示图像

    def image_choose(self):
        # 根据配置参数和文件路径处理并显示图像
        if self.parameters and self.file_path:  # 如果有配置参数和文件路径
            if self.is_raw:  # 如果是原始图像
                data = process_raw_file(self.file_path, self.parameters)  # 处理RAW文件
            else:  # 如果是YUV图像
                data = get_yuv_rgb(self.file_path, self.parameters)  # 获取YUV图像的RGB数据
            self.show_rgb(data)  # 显示RGB图像
            self.show_info()  # 显示图像信息

    def show_info(self):
        # 显示图像信息
        if self.is_raw:  # 如果是原始图像
            self.info = RAW_INFO(parameters=self.parameters, file_path=self.file_path)  # 创建原始图像信息对象
        else:  # 如果是YUV图像
            self.info = YUV_INFO(parameters=self.parameters, file_path=self.file_path)  # 创建YUV图像信息对象
        self.info.clear_pix.connect(self.scene.clear)  # 连接清除像素信号
        self.info.clear_pix.connect(self.reload)  # 连接重新加载信号
        self.info.show()  # 显示图像信息

    def reload(self):
        # 重新加载并显示图像
        self.scene.clear()  # 清除当前场景
        if self.is_raw:  # 如果是原始图像
            data = process_raw_file(self.ui.RawPath.text(), self.parameters)  # 处理RAW文件
            self.show_rgb(data)  # 显示RGB图像
        else:  # 如果是YUV图像
            data = get_yuv_rgb(self.ui.YuvPath.text(), self.parameters)  # 获取YUV图像的RGB数据
            self.show_rgb(data)  # 显示RGB图像

    def show_rgb(self, data):
        # 显示RGB图像数据
        self.data = data  # 设置图像数据
        try:
            height, width = data.shape[:2]  # 获取图像的高度和宽度
            if data.dtype == np.uint16:  # 如果数据类型是uint16
                min_val = np.min(data)  # 获取最小值
                max_val = np.max(data)  # 获取最大值
                if max_val == min_val:  # 如果最大值和最小值相同
                    normalized_data = data  # 不进行归一化
                else:
                    normalized_data = ((data - min_val) / (max_val - min_val)) * 255  # 归一化数据到0-255
                normalized_data = np.clip(normalized_data, 0, 255)  # 限制数据范围
                data = np.uint8(normalized_data)  # 转换为uint8类型
            if len(data.shape) != 3 or data.shape[2] != 3:  # 检查数据是否为RGB格式
                raise ValueError("Invalid data format for RGB.")
            q_image = QImage(data, width, height, width * 3, QImage.Format.Format_RGB888)  # 创建QImage对象
            if q_image.isNull():  # 如果QImage对象为空
                raise ValueError("QImage creation failed")
            pixmap = QPixmap.fromImage(q_image)  # 从QImage创建QPixmap对象
            scene = QGraphicsScene()  # 创建QGraphicsScene对象
            scene.addItem(QGraphicsPixmapItem(pixmap))  # 将QPixmap添加到场景中
            self.image_view.setScene(scene)  # 设置图像视图的场景
            self.ui.showView.setViewport(self.image_view)  # 设置显示视图的端口
            self.image_view.set_parent(self)  # 设置图像视图的父对象
            self.scene = scene  # 设置当前场景
            self.has_image_displayed = True  # 标记已显示图像
        except Exception as e:  # 捕获并打印异常
            print(e)

    def show_RGB(self, file_path):
        # 从文件路径显示RGB图像
        try:
            img = cv2.imread(file_path)  # 读取图像文件
            if img is None:  # 如果图像为空
                raise ValueError(f"Failed to read image at {file_path}")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将BGR图像转换为RGB
            height, width = img.shape[:2]  # 获取图像的高度和宽度
            q_image = QImage(img, width, height, width * 3, QImage.Format.Format_RGB888)  # 创建QImage对象
            if q_image.isNull():  # 如果QImage对象为空
                raise ValueError("QImage creation failed")
            pixmap = QPixmap.fromImage(q_image)  # 从QImage创建QPixmap对象
            scene = QGraphicsScene()  # 创建QGraphicsScene对象
            scene.addItem(QGraphicsPixmapItem(pixmap))  # 将QPixmap添加到场景中
            self.image_view.setScene(scene)  # 设置图像视图的场景
            self.ui.showView.setViewport(self.image_view)  # 设置显示视图的端口
            self.image_view.set_parent(self)  # 设置图像视图的父对象
            self.scene = scene  # 设置当前场景
            self.has_image_displayed = True  # 标记已显示图像
        except Exception as e:  # 捕获并打印异常
            print(e)

    def display_metadata(self, x, y, rgb, hsl, ycbcr):
        # 显示图像的元数据
        metadata_text = f"Position: ({x}, {y}) | RGB: {rgb} | HSL: {hsl} | YCbCr: {ycbcr}"  # 格式化元数据文本
        self.ui.label.setText(metadata_text)  # 将元数据文本设置到标签中

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setAcceptDrops(True)
    widget.show()
    sys.exit(app.exec())