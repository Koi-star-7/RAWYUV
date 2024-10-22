# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGroupBox, QHBoxLayout,
                               QLineEdit, QPushButton, QVBoxLayout,
                               QLabel, QWidget)

from ImageView import ImageView
from ui_compare import Ui_Compare


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)

        # 主垂直布局
        self.verticalLayout_3 = QVBoxLayout(Widget)

        # 顶部水平布局
        self.horizontalLayout_3 = QHBoxLayout()

        # RAW 组框及内部布局
        self.groupBox_RAW = QGroupBox(Widget)
        self.groupBox_RAW.setObjectName(u"groupBox_RAW")
        self.verticalLayout_raw = QVBoxLayout(self.groupBox_RAW)
        self.horizontalLayout_raw = QHBoxLayout()
        self.RawPath = QLineEdit(self.groupBox_RAW)
        self.RawPath.setObjectName(u"RawPath")
        self.RawC = QPushButton(self.groupBox_RAW)
        self.RawC.setObjectName(u"RawC")
        self.horizontalLayout_raw.addWidget(self.RawPath)
        self.horizontalLayout_raw.addWidget(self.RawC)
        self.verticalLayout_raw.addLayout(self.horizontalLayout_raw)

        # YUV 组框及内部布局
        self.groupBox_YUV = QGroupBox(Widget)
        self.groupBox_YUV.setObjectName(u"groupBox_YUV")
        self.verticalLayout_yuv = QVBoxLayout(self.groupBox_YUV)
        self.horizontalLayout_yuv = QHBoxLayout()
        self.YuvPath = QLineEdit(self.groupBox_YUV)
        self.YuvPath.setObjectName(u"YuvPath")
        self.YuvC = QPushButton(self.groupBox_YUV)
        self.YuvC.setObjectName(u"YuvC")
        self.horizontalLayout_yuv.addWidget(self.YuvPath)
        self.horizontalLayout_yuv.addWidget(self.YuvC)
        self.verticalLayout_yuv.addLayout(self.horizontalLayout_yuv)

        # 创建按钮垂直布局
        self.buttonLayout_1 = QVBoxLayout()
        self.one_to_one = QPushButton(Widget)
        self.one_to_one.setObjectName(u"one_to_one")
        self.buttonLayout_1.addWidget(self.one_to_one)

        self.compare = QPushButton(Widget)
        self.compare.setObjectName(u"compare")
        self.buttonLayout_1.addWidget(self.compare)

        self.buttonLayout_2 = QVBoxLayout()
        self.convert = QPushButton(Widget)
        self.convert.setObjectName(u"convert")
        self.buttonLayout_2.addWidget(self.convert)

        self.gridline = QPushButton(Widget)
        self.gridline.setObjectName(u"gridline")
        self.buttonLayout_2.addWidget(self.gridline)

        # 将组框和按钮布局添加到顶部水平布局
        self.horizontalLayout_3.addWidget(self.groupBox_RAW)
        self.horizontalLayout_3.addWidget(self.groupBox_YUV)
        self.horizontalLayout_3.addLayout(self.buttonLayout_1)
        self.horizontalLayout_3.addLayout(self.buttonLayout_2)

        # 将顶部布局添加到主垂直布局
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        # 图像视图及提示标签布局
        self.showView = ImageView()
        self.hintLabel = QLabel(self.showView)
        self.hintLabel.setAlignment(Qt.AlignCenter)
        self.hintLabel.setStyleSheet("color: gray;")
        font = QFont()
        font.setPointSize(20)
        self.hintLabel.setFont(font)
        self.hintLabel.setText("请将.jpg.png.bmp 的图片拖动至此以打开")
        layout = QVBoxLayout(self.showView)
        layout.addStretch(1)
        layout.addWidget(self.hintLabel)
        layout.addStretch(1)

        # 将图像视图添加到主垂直布局
        self.verticalLayout_3.addWidget(self.showView)

        self.label = QLabel(Widget)
        self.verticalLayout_3.addWidget(self.label)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_RAW.setTitle(QCoreApplication.translate("Widget", u"RAW", None))
        self.RawC.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9Raw", None))
        self.groupBox_YUV.setTitle(QCoreApplication.translate("Widget", u"YUV", None))
        self.YuvC.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9YUV", None))
        self.convert.setText(QCoreApplication.translate("Widget", u"\u8f6c\u6362", None))
        self.one_to_one.setText(QCoreApplication.translate("Widget", u"1:1", None))
        self.gridline.setText(QCoreApplication.translate("Widget", u"\u7f51\u683c\u7ebf", None))
        self.compare.setText(QCoreApplication.translate("Widget", u"对比模式", None))