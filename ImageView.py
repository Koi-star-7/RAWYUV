from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsRectItem

# 显示和处理图像
class ImageView(QtWidgets.QGraphicsView):
    def __init__(self):
        super(ImageView, self).__init__()  # 调用父类的初始化方法
        # self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 设置水平滚动条始终不显示
        # self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 设置垂直滚动条始终不显示
        # self.setDragMode(QtWidgets.QGraphicsView.NoDrag)  # 设置拖动模式为无拖动
        self.start_point = None  # 初始化起始点为None
        self.selected_rect_item = None  # 初始化选中的矩形项为None
        self.rect_pen = QPen(QColor(255, 0, 0))  # 创建一个红色的画笔用于绘制矩形
        self.label = QtWidgets.QLabel(self)  #创建一个标签并设置父组件为当前对象
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0.7); color: black;")  # 设置标签的样式表，包括背景颜色半透明白色和黑色文字
        self.label.hide()  # 隐藏标签
        self.setMouseTracking(True)
        self.is_selected = False

    def setSelected(self, selected):
        self.is_selected = selected

    def set_parent(self, parent):
        # 设置父组件
        self.parent_widget = parent

    def wheelEvent(self, event):
        # 如果场景中没有任何项，则直接返回，不进行任何处理
        if len(self.scene().items()) == 0:
            return
        # 获取鼠标滚轮事件的当前位置
        curPoint = event.position()

        # 将视图坐标转换为场景坐标
        scenePos = self.mapToScene(QtCore.QPoint(int(curPoint.x()), int(curPoint.y())))

        # 获取视图的宽高
        viewWidth = self.viewport().width()
        viewHeight = self.viewport().height()

        # 计算水平和垂直方向上的比例
        hScale = curPoint.x() / viewWidth
        vScale = curPoint.y() / viewHeight

        # 获取滚轮的滚动值
        wheelDeltaValue = event.angleDelta().y()

        # 获取当前的缩放因子
        scaleFactor = self.transform().m11()

        # 如果缩放因子小于0.05且滚轮向下滚动，或者缩放因子大于50且滚轮向上滚动，则不进行缩放操作
        if (scaleFactor < 0.05 and wheelDeltaValue < 0) or (scaleFactor > 50 and wheelDeltaValue > 0):
            return
        # 如果滚轮向上滚动
        if wheelDeltaValue > 0:
            # 进行放大操作，缩放因子为1.2
            self.scale(1.2, 1.2)
        # 如果滚轮向下滚动
        else:
            # 进行缩小操作，缩放因子为1/1.2
            self.scale(1.0 / 1.2, 1.0 / 1.2)

        # 将场景坐标经过当前变换后得到新的视图坐标
        viewPoint = self.transform().map(scenePos)

        # 设置水平滚动条的值，使得缩放后鼠标位置相对视图的位置保持不变
        self.horizontalScrollBar().setValue(int(viewPoint.x() - viewWidth * hScale))
        # 设置垂直滚动条的值，使得缩放后鼠标位置相对视图的位置保持不变
        self.verticalScrollBar().setValue(int(viewPoint.y() - viewHeight * vScale))
        # 更新视图
        self.update()

    def mousePressEvent(self, event):
        # 判断按下的是否为鼠标右键
        if event.button() == QtCore.Qt.RightButton:
            # 如果已经存在选中的矩形项
            if self.selected_rect_item is not None:
                # 检查选中的矩形项是否在场景中的项目列表中，如果是则移除
                if self.scene().items().count(self.selected_rect_item) > 0:
                    self.scene().removeItem(self.selected_rect_item)

            # 记录鼠标按下的起点
            self.start_point = event.pos()

            # 设置拖动模式为橡皮筋拖动
            self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)

            # 隐藏标签
            self.label.hide()
        # 判断按下的是否为鼠标左键和空格键
        elif event.button() == QtCore.Qt.LeftButton:
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

        # 调用父类的鼠标按下事件处理方式
        super(ImageView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):

        # 如果起始点不为None且当前拖动模式为橡皮筋拖动
        if self.start_point is not None and self.dragMode() == QtWidgets.QGraphicsView.RubberBandDrag:
            # 获取鼠标移动的终点
            end_point = event.pos()

            # 根据起始点和终点计算出矩形区域，并进行规范化处理
            rect = QtCore.QRectF(self.mapToScene(self.start_point), self.mapToScene(end_point)).normalized()

            # 获取矩形的宽高，并转化为整数
            width = int(rect.width())
            height = int(rect.height())

            # 在标签中显示宽高
            self.label.setText(f"Width: {int(width)} Height: {int(height)}")

            # 调整标签大小
            self.label.adjustSize()

            # 将标签移动到鼠标位置右侧和下方一定距离处
            self.label.move(event.pos() + QtCore.QPoint(10, 10))

            # 显示标签
            self.label.show()

        else:
            item = self.itemAt(event.pos())
            if isinstance(item, QGraphicsPixmapItem):
                # 将视图坐标转换为场景坐标
                scene_pos = self.mapToScene(event.pos())

                # 将场景坐标转换为像素图中的坐标
                pixmap_pos = item.pixmap().toImage().rect().topLeft() + scene_pos.toPoint()
                if pixmap_pos.x() >= 0 and pixmap_pos.y() >= 0 and pixmap_pos.x() < item.pixmap().width() and pixmap_pos.y() < item.pixmap().height():
                    # 获取鼠标在像素图中的x和y坐标
                    x, y = int(pixmap_pos.x()), int(pixmap_pos.y())

                    # 获取像素颜色
                    color = item.pixmap().toImage().pixelColor(pixmap_pos)

                    # 计算平均 RGB、HSL 和 YCbCr 颜色
                    avg_rgb = self.calculate_average_color(
                        item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))
                    avg_hsl = self.calculate_average_hsl(
                        item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))
                    avg_ycbcr = self.calculate_average_ycbcr(
                        item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))

                    # 将鼠标位置坐标和颜色信息传递给父组件进行显示
                    self.parent_widget.display_metadata(x, y, avg_rgb, avg_hsl, avg_ycbcr)

        # 调用父类的鼠标移动事件处理方法
        super(ImageView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.setMouseTracking(False)
        # 判断释放的是否为鼠标右键
        if event.button() == QtCore.Qt.RightButton:
            # 记录鼠标释放的终点
            self.end_point = event.pos()

            # 设置拖动模式为无拖动
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

            # 获取鼠标释放位置的图形项
            item = self.itemAt(event.pos())

            # 判断图形项是否为QGraphicsPixmapItem类型
            if isinstance(item, QGraphicsPixmapItem):
                # 根据起始点和终点计算出矩形区域，并进行规范化处理
                rect = QtCore.QRectF(self.mapToScene(self.start_point), self.mapToScene(self.end_point)).normalized()

                # 从图形项的像素图中复制出选中的区域
                selected_image = item.pixmap().copy(rect.toRect())

                # 计算选中区域的平均RGB、HSL和YCbCr颜色
                avg_rgb = self.calculate_average_color(selected_image)
                avg_hsl = self.calculate_average_hsl(selected_image)
                avg_ycbcr = self.calculate_average_ycbcr(selected_image)

                # 获取矩形框左上角的坐标
                top_left = rect.topLeft()
                x = round(top_left.x(), 2)
                y = round(top_left.y(), 2)

                # 如果有父窗口，调用父窗口的方法显示元数据
                self.parent_widget.display_metadata(x, y, avg_rgb, avg_hsl, avg_ycbcr)
                # 创建一个矩形图形项表示选中区域
                self.selected_rect_item = QGraphicsRectItem(rect)

                # 设置矩形的边框样式
                self.selected_rect_item.setPen(self.rect_pen)

                # 将矩形图形项添加到场景中
                self.scene().addItem(self.selected_rect_item)

            # 隐藏标签
            self.label.hide()

        # 判断释放的是否为鼠标左键
        elif event.button() == QtCore.Qt.LeftButton:
            # 如果已经存在选中的矩形项
            if self.selected_rect_item is not None:
                # 检查选中的矩形项是否在场景中的项目列表中，如果是则移除
                if self.scene().items().count(self.selected_rect_item) > 0:
                    self.scene().removeItem(self.selected_rect_item)
            self.setMouseTracking(True)
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            super(ImageView, self).mouseReleaseEvent(event)

    def calculate_average_color(self, pixmap):
        # 将传入的像素图转换为QImage对象
        image = pixmap.toImage()

        # 初始化累计的红色、绿色、蓝色分量总和为0
        total_red = 0
        total_green = 0
        total_blue = 0

        # 初始化像素数量为0
        pixel_count = 0

        # 获取图像的宽高
        width = image.width()
        height = image.height()

        # 在x和y方向上采样步长，确保至少为1，最多为宽高的1/100
        step_x = max(1, width // 100)
        step_y = max(1, height // 100)

        # 遍历图像，按照采样步长进行采样
        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                # 获取当前像素的颜色
                color = image.pixelColor(x, y)

                # 累计三种颜色的分量
                total_red += color.red()
                total_green += color.green()
                total_blue += color.blue()

                # 增加像素数量计数
                pixel_count += 1

        # 如果有采样的像素
        if pixel_count > 0:
            # 计算平均红色、绿色、蓝色分量并返回
            return total_red // pixel_count, total_green // pixel_count, total_blue // pixel_count
        else:
            # 如果没有采样的像素，返回默认的黑色（0, 0, 0）
            return 0, 0, 0

    def calculate_average_hsl(self, pixmap):
        # 将传入的像素图转换为 QImage 对象
        image = pixmap.toImage()

        # 获取图像的宽高
        width = image.width()
        height = image.height()

        # 如果传入的范围是一个像素点
        if width == 1 and height == 1:
            color = image.pixelColor(0, 0)
            hsl = color.getHsl()
            # 确保色相在有效范围内
            hue = hsl[0] if hsl[0] >= 0 else 0
            saturation = round((hsl[1] / 255) * 100, 1)
            lightness = round((hsl[2] / 255) * 100, 1)
            return hue, f'{saturation}%', f'{lightness}%'

        # 初始化累计的色相、饱和度、亮度总和为 0
        total_hue = 0
        total_saturation = 0
        total_lightness = 0

        # 初始化像素数量为 0
        pixel_count = 0

        # 计算在 x 和 y 方向上的采样步长，确保至少为 1，最多为宽度或高度的 1/100
        step_x = max(1, width // 100)
        step_y = max(1, height // 100)

        # 遍历图像，按照采样步长进行采样
        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                # 获取当前像素的颜色
                color = image.pixelColor(x, y)

                # 获取颜色的 HSL 值
                hsl = color.getHsl()

                # 累计色相
                total_hue += hsl[0]

                # 累计饱和度
                total_saturation += hsl[1]

                # 累计亮度
                total_lightness += hsl[2]

                # 增加像素数量计数
                pixel_count += 1

        # 如果有采样的像素
        if pixel_count > 0:
            # 计算平均色相
            avg_hue = total_hue // pixel_count

            # 计算平均饱和度并转换为百分比形式，保留一位小数
            avg_saturation = (total_saturation / pixel_count) / 255 * 100
            avg_saturation = round(avg_saturation, 1)

            # 计算平均亮度并转换为百分比形式，保留一位小数
            avg_lightness = (total_lightness / pixel_count) / 255 * 100
            avg_lightness = round(avg_lightness, 1)

            return avg_hue, f'{avg_saturation}%', f'{avg_lightness}%'
        else:
            # 如果没有采样的像素，返回默认的（0, 0, 0）
            return 0, '0%', '0%'

    def calculate_average_ycbcr(self, pixmap):
        # 将传入的像素图转换为 QImage 对象
        image = pixmap.toImage()

        # 初始化累计的红色、绿色、蓝色分量总和为 0
        total_red = 0
        total_green = 0
        total_blue = 0

        # 初始化Y、Cb、Cr分量总和为0
        total_y = 0
        total_cb = 0
        total_cr = 0

        # 初始化像素数量为 0
        pixel_count = 0

        # 获取图像的宽高
        width = image.width()
        height = image.height()

        # 在 x 和 y 方向上采样步长，确保至少为 1，最多为宽度或高度的 1/100
        step_x = max(1, width // 100)
        step_y = max(1, height // 100)

        # 遍历图像，按照采样步长进行采样
        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                # 获取当前像素的颜色
                color = image.pixelColor(x, y)

                # 累计三种颜色的分量
                total_red += color.red()
                total_green += color.green()
                total_blue += color.blue()

                # 增加像素数量计数
                pixel_count += 1

        # 计算平均的红、绿、蓝分量
        r = total_red // pixel_count
        g = total_green // pixel_count
        b = total_blue // pixel_count

        # 初始化像素数量为 0
        pixel_count = 0

        # 获取父窗口
        widget = self.parent_widget if hasattr(self, 'parent_widget') else None

        # 判断是否为raw图像
        is_raw = widget.is_raw if widget and hasattr(widget, 'is_raw') else False

        # 获取参数字典
        parameters = widget.parameters if widget and hasattr(widget, 'parameters') else None

        # 获取TV范围参数
        TV_range = parameters['TV_range'] if parameters and 'TV_range' in parameters else False

        # 获取标准参数
        standard = parameters['standard'] if parameters and 'standard' in parameters else None

        # 如果是 RAW 图
        if is_raw:
            # 计算RAW图的Y、Cb、Cr值
            raw_y = 0.299 * r + 0.587 * g + 0.114 * b
            raw_cb = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
            raw_cr = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

            # 累计 RAW 图的Y、Cb、Cr的分量
            total_y += raw_y
            total_cb += raw_cb
            total_cr += raw_cr

            # 增加像素数量计数
            pixel_count += 1
        else:
            # 如果是 TV 范围
            if TV_range:
                # 根据不同的标准计算Y、Cb、Cr值
                if standard == 'BT.601':
                    yuv_y = 0.2568 * r + 0.5041 * g + 0.0979 * b + 16
                    yuv_cb = -0.1482 * r - 0.2910 * g + 0.4392 * b + 128
                    yuv_cr = 0.4392 * r - 0.3678 * g - 0.0714 * b + 128

                    # 累计 YUV 图的Y、Cb、Cr的分量
                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    # 增加像素数量计数
                    pixel_count += 1
                elif standard == 'BT.709':
                    yuv_y = 0.1826 * r + 0.6142 * g + 0.0620 * b + 16
                    yuv_cb = -0.1006 * r - 0.3386 * g + 0.4392 * b + 128
                    yuv_cr = 0.4392 * r - 0.3989 * g - 0.0403 * b + 128

                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    pixel_count += 1
                elif standard == 'BT.2020':
                    yuv_y = 0.2257 * r + 0.5828 * g + 0.0501 * b + 16
                    yuv_cb = -0.1225 * r - 0.3166 * g + 0.4392 * b + 128
                    yuv_cr = 0.4392 * r - 0.4027 * g - 0.0366 * b + 128

                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    pixel_count += 1
            else:
                # 不是 TV 类型时，根据不同的标准计算Y、Cb、Cr值
                if standard == 'BT.601':
                    yuv_y = 0.299 * r + 0.587 * g + 0.114 * b
                    yuv_cb = -0.14713 * r - 0.28886 * g + 0.436 * b + 128
                    yuv_cr = 0.615 * r - 0.51499 * g - 0.10001 * b + 128

                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    pixel_count += 1
                elif standard == 'BT.709':
                    yuv_y = 0.1826 * r + 0.6142 * g + 0.0620 * b
                    yuv_cb = -0.1006 * r - 0.3386 * g + 0.4392 * b + 128
                    yuv_cr = 0.4392 * r - 0.3989 * g - 0.0403 * b + 128

                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    pixel_count += 1
                elif standard == 'BT.2020':
                    yuv_y = 0.2627 * r + 0.6780 * g + 0.0593 * b
                    yuv_cb = -0.13963 * r - 0.36037 * g + 0.5 * b + 128
                    yuv_cr = 0.5 * r - 0.45979 * g - 0.04021 * b + 128

                    total_y += yuv_y
                    total_cb += yuv_cb
                    total_cr += yuv_cr

                    pixel_count += 1

        # 如果像素数量大于 0，返回平均的 Y、Cb、Cr 值，否则返回 0
        if pixel_count > 0:
            return total_y // pixel_count, total_cb // pixel_count, total_cr // pixel_count
        else:
            return 0, 0, 0

    """
    item = self.itemAt(event.pos())
    if isinstance(item, QGraphicsPixmapItem):
        # 将视图坐标转换为场景坐标
        scene_pos = self.mapToScene(event.pos())

        # 将场景坐标转换为像素图中的坐标
        pixmap_pos = item.pixmap().toImage().rect().topLeft() + scene_pos.toPoint()
        if pixmap_pos.x() >= 0 and pixmap_pos.y() >= 0 and pixmap_pos.x() < item.pixmap().width() and pixmap_pos.y() < item.pixmap().height():
            # 获取鼠标在像素图中的x和y坐标
            x, y = int(pixmap_pos.x()), int(pixmap_pos.y())

            # 获取像素颜色
            color = item.pixmap().toImage().pixelColor(pixmap_pos)

            # 计算平均 RGB、HSL 和 YCbCr 颜色
            avg_rgb = self.calculate_average_color(
                item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))
            avg_hsl = self.calculate_average_hsl(
                item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))
            avg_ycbcr = self.calculate_average_ycbcr(
                item.pixmap().copy(QtCore.QRect(pixmap_pos, QtCore.QSize(1, 1))))

            # 将鼠标位置坐标和颜色信息传递给父组件进行显示
            self.parent_widget.display_metadata(x, y, avg_rgb, avg_hsl, avg_ycbcr)
    """