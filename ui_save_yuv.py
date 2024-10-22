# 保存为yuv图时的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_yuv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_save_yuv_Form(object):
    def __init__(self):
        self.bayer = None
        self.bit = None
        self.compress = None

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 320)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.head = QComboBox(Form)
        self.head.addItem("")
        self.head.addItem("")
        self.head.addItem("")
        self.head.setObjectName(u"head")

        self.horizontalLayout_2.addWidget(self.head)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.format = QComboBox(Form)
        self.format.setObjectName(u"format")

        self.horizontalLayout.addWidget(self.format)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.standard = QComboBox(Form)
        self.standard.addItem("")
        self.standard.addItem("")
        self.standard.addItem("")
        self.standard.setObjectName(u"standard")

        self.horizontalLayout_4.addWidget(self.standard)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.TV_type = QRadioButton(Form)
        self.TV_type.setObjectName(u"TV_type")

        self.verticalLayout.addWidget(self.TV_type)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"yuv head", None))
        self.head.setItemText(0, QCoreApplication.translate("Form", u"4:4:4", None))
        self.head.setItemText(1, QCoreApplication.translate("Form", u"4:2:2", None))
        self.head.setItemText(2, QCoreApplication.translate("Form", u"4:2:0", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"yuv format", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"standard", None))
        self.standard.setItemText(0, QCoreApplication.translate("Form", u"BT.601", None))
        self.standard.setItemText(1, QCoreApplication.translate("Form", u"BT.709", None))
        self.standard.setItemText(2, QCoreApplication.translate("Form", u"BT.2020", None))

        self.TV_type.setText(QCoreApplication.translate("Form", u"TV type", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"save", None))
    # retranslateUi

