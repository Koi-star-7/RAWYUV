# 打开yuv图后 配置yuv图的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yuv_info.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_yuv_info(object):
    def setupUi(self, yuv_info):
        if not yuv_info.objectName():
            yuv_info.setObjectName(u"yuv_info")
        yuv_info.resize(222, 366)
        self.verticalLayout = QVBoxLayout(yuv_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(yuv_info)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.width = QLabel(yuv_info)
        self.width.setObjectName(u"width")

        self.horizontalLayout.addWidget(self.width)

        self.label_3 = QLabel(yuv_info)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(yuv_info)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.height = QLabel(yuv_info)
        self.height.setObjectName(u"height")

        self.horizontalLayout_2.addWidget(self.height)

        self.label_4 = QLabel(yuv_info)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(yuv_info)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pattern = QLabel(yuv_info)
        self.pattern.setObjectName(u"pattern")

        self.horizontalLayout_3.addWidget(self.pattern)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(yuv_info)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(yuv_info)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(yuv_info)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.comboBox = QComboBox(yuv_info)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.groupBox = QGroupBox(yuv_info)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Y_channel = QCheckBox(self.groupBox)
        self.Y_channel.setObjectName(u"Y_channel")

        self.horizontalLayout_6.addWidget(self.Y_channel)

        self.Cr_channel = QCheckBox(self.groupBox)
        self.Cr_channel.setObjectName(u"Cr_channel")

        self.horizontalLayout_6.addWidget(self.Cr_channel)

        self.Cb_channel = QCheckBox(self.groupBox)
        self.Cb_channel.setObjectName(u"Cb_channel")

        self.horizontalLayout_6.addWidget(self.Cb_channel)


        self.verticalLayout.addWidget(self.groupBox)

        self.checkBox = QCheckBox(yuv_info)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.reload = QPushButton(yuv_info)
        self.reload.setObjectName(u"reload")

        self.verticalLayout.addWidget(self.reload)


        self.retranslateUi(yuv_info)

        QMetaObject.connectSlotsByName(yuv_info)
    # setupUi

    def retranslateUi(self, yuv_info):
        yuv_info.setWindowTitle(QCoreApplication.translate("yuv_info", u"Form", None))
        self.label.setText(QCoreApplication.translate("yuv_info", u"width", None))
        self.width.setText("")
        self.label_3.setText(QCoreApplication.translate("yuv_info", u"pixels", None))
        self.label_2.setText(QCoreApplication.translate("yuv_info", u"height", None))
        self.height.setText("")
        self.label_4.setText(QCoreApplication.translate("yuv_info", u"pixels", None))
        self.label_5.setText(QCoreApplication.translate("yuv_info", u"pattern", None))
        self.pattern.setText("")
        self.label_6.setText(QCoreApplication.translate("yuv_info", u"standard ", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("yuv_info", u"BT.601", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("yuv_info", u"BT.709", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("yuv_info", u"BT.2020", None))

        self.label_7.setText(QCoreApplication.translate("yuv_info", u"interpolation", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("yuv_info", u"nearest", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("yuv_info", u"cubic", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("yuv_info", u"linear", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("yuv_info", u"area", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("yuv_info", u"linear_exact", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("yuv_info", u"nearest_exact", None))

        self.groupBox.setTitle(QCoreApplication.translate("yuv_info", u"Channel", None))
        self.Y_channel.setText(QCoreApplication.translate("yuv_info", u"Y", None))
        self.Cr_channel.setText(QCoreApplication.translate("yuv_info", u"Cr", None))
        self.Cb_channel.setText(QCoreApplication.translate("yuv_info", u"Cb", None))
        self.checkBox.setText(QCoreApplication.translate("yuv_info", u"TV_range", None))
        self.reload.setText(QCoreApplication.translate("yuv_info", u"reload", None))
    # retranslateUi

