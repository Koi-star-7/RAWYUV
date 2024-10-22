# 保存为raw图时的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_raw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)


class Ui_save_raw_Form(object):
    def __init__(self):
        self.compress = None
        self.pushButton = None
        self.bit = None

    def setupUi(self, Ui_save_raw_Form):
        if not Ui_save_raw_Form.objectName():
            Ui_save_raw_Form.setObjectName(u"Ui_save_raw_Form")
        Ui_save_raw_Form.resize(240, 320)
        self.verticalLayout_2 = QVBoxLayout(Ui_save_raw_Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Ui_save_raw_Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.bayer = QComboBox(Ui_save_raw_Form)
        self.bayer.addItem("")
        self.bayer.addItem("")
        self.bayer.addItem("")
        self.bayer.addItem("")
        self.bayer.setObjectName(u"bayer")

        self.horizontalLayout_2.addWidget(self.bayer)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.compress = QRadioButton(Ui_save_raw_Form)
        self.compress.setObjectName(u"compress")

        self.horizontalLayout.addWidget(self.compress)

        self.bit = QComboBox(Ui_save_raw_Form)
        self.bit.addItem("")
        self.bit.addItem("")
        self.bit.addItem("")
        self.bit.setObjectName(u"bit")

        self.horizontalLayout.addWidget(self.bit)

        self.label_2 = QLabel(Ui_save_raw_Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Ui_save_raw_Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Ui_save_raw_Form)

        QMetaObject.connectSlotsByName(Ui_save_raw_Form)

    # setupUi

    def retranslateUi(self, Ui_save_raw_Form):
        Ui_save_raw_Form.setWindowTitle(QCoreApplication.translate("Ui_save_raw_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Ui_save_raw_Form", u"Bayer Pattern", None))
        self.bayer.setItemText(0, QCoreApplication.translate("Ui_save_raw_Form", u"RGGB", None))
        self.bayer.setItemText(1, QCoreApplication.translate("Ui_save_raw_Form", u"BGGR", None))
        self.bayer.setItemText(2, QCoreApplication.translate("Ui_save_raw_Form", u"GRBG", None))
        self.bayer.setItemText(3, QCoreApplication.translate("Ui_save_raw_Form", u"GBRG", None))

        self.compress.setText(QCoreApplication.translate("Ui_save_raw_Form", u"compress", None))
        self.bit.setItemText(0, QCoreApplication.translate("Ui_save_raw_Form", u"10", None))
        self.bit.setItemText(1, QCoreApplication.translate("Ui_save_raw_Form", u"12", None))
        self.bit.setItemText(2, QCoreApplication.translate("Ui_save_raw_Form", u"14", None))

        self.label_2.setText(QCoreApplication.translate("Ui_save_raw_Form", u"bit", None))
        self.pushButton.setText(QCoreApplication.translate("Ui_save_raw_Form", u"save_raw", None))
    # retranslateUi
