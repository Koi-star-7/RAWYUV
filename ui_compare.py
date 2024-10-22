# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QGroupBox, QLineEdit, QPushButton, QVBoxLayout, QLabel, QHBoxLayout)

from ImageView import ImageView

class Ui_Compare(object):
    def setupUi(self, Compare):
        if not Compare.objectName():
            Compare.setObjectName(u"Widget")
        Compare.resize(1280, 720)

        self.mainVerticalLayout = QVBoxLayout(Compare)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")

        self.topHorizontalLayout = QHBoxLayout()
        self.topHorizontalLayout.setObjectName(u"topHorizontalLayout")

        self.gridline = QPushButton(Compare)
        self.gridline.setObjectName(u"gridline")
        self.one_to_one = QPushButton(Compare)
        self.one_to_one.setObjectName(u"one_to_one")

        self.groupBox_RAW = QGroupBox(Compare)
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

        self.groupBox_YUV = QGroupBox(Compare)
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

        button_size = 50
        self.gridline.setFixedSize(button_size, button_size)
        self.one_to_one.setFixedSize(button_size, button_size)

        self.topHorizontalLayout.addWidget(self.groupBox_RAW)
        self.topHorizontalLayout.addWidget(self.groupBox_YUV)
        self.topHorizontalLayout.addWidget(self.one_to_one)
        self.topHorizontalLayout.addWidget(self.gridline)

        self.mainVerticalLayout.addLayout(self.topHorizontalLayout)

        self.imageHorizontalLayout = QHBoxLayout()
        self.imageHorizontalLayout.setObjectName(u"imageHorizontalLayout")

        self.showView1 = ImageView()
        self.showView1.setObjectName(u"showView1")

        self.imageHorizontalLayout.addWidget(self.showView1)

        self.mainVerticalLayout.addLayout(self.imageHorizontalLayout)

        self.label = QLabel(Compare)
        self.label.setObjectName(u"label")
        self.mainVerticalLayout.addWidget(self.label)

        self.showView1.is_selected = False

        self.retranslateUi(Compare)

        QMetaObject.connectSlotsByName(Compare)

    def retranslateUi(self, Compare):
        Compare.setWindowTitle(QCoreApplication.translate("Compare", u"Compare", None))
        self.groupBox_RAW.setTitle(QCoreApplication.translate("Compare", u"RAW", None))
        self.RawC.setText(QCoreApplication.translate("Compare", u"\u9009\u62e9Raw", None))
        self.groupBox_YUV.setTitle(QCoreApplication.translate("Compare", u"YUV", None))
        self.YuvC.setText(QCoreApplication.translate("Compare", u"\u9009\u62e9YUV", None))
        self.one_to_one.setText(QCoreApplication.translate("Compare", u"1:1", None))
        self.gridline.setText(QCoreApplication.translate("Compare", u"\u7f51\u683c\u7ebf", None))