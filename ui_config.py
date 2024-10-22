# 打开raw图时的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox,
                               QDialogButtonBox, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QRadioButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 320)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rg = QRadioButton(self.groupBox)
        self.rg.setObjectName(u"rg")

        self.horizontalLayout.addWidget(self.rg)

        self.bg = QRadioButton(self.groupBox)
        self.bg.setObjectName(u"bg")

        self.horizontalLayout.addWidget(self.bg)

        self.gb = QRadioButton(self.groupBox)
        self.gb.setObjectName(u"gb")

        self.horizontalLayout.addWidget(self.gb)

        self.gr = QRadioButton(self.groupBox)
        self.gr.setObjectName(u"gr")

        self.horizontalLayout.addWidget(self.gr)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.height_2 = QLineEdit(Dialog)
        self.height_2.setObjectName(u"height_2")

        self.horizontalLayout_2.addWidget(self.height_2)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.height = QLineEdit(Dialog)
        self.height.setObjectName(u"height")

        self.horizontalLayout_3.addWidget(self.height)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Raw Pattern", None))
        self.rg.setText(QCoreApplication.translate("Dialog", u"RG", None))
        self.bg.setText(QCoreApplication.translate("Dialog", u"BG", None))
        self.gb.setText(QCoreApplication.translate("Dialog", u"GB", None))
        self.gr.setText(QCoreApplication.translate("Dialog", u"GR", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Bit Dipth", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"10", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"12", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"14", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"16", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"pixels", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"width  ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"pixels", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Bigger-endian byte order", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"MIPI Raw", None))
    # retranslateUi