# 打开raw图后 配置raw图的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'raw_info.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QCheckBox, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QTableView, QVBoxLayout)


class Ui_Raw_info(object):
    def setupUi(self, Raw_info):
        if not Raw_info.objectName():
            Raw_info.setObjectName(u"Raw_info")
        Raw_info.resize(243, 474)
        self.verticalLayout_3 = QVBoxLayout(Raw_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Raw_info)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.bit_depth = QLabel(Raw_info)
        self.bit_depth.setObjectName(u"bit_depth")

        self.horizontalLayout_4.addWidget(self.bit_depth)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Raw_info)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.height = QLabel(Raw_info)
        self.height.setObjectName(u"height")

        self.horizontalLayout_2.addWidget(self.height)

        self.label_4 = QLabel(Raw_info)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Raw_info)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.width = QLabel(Raw_info)
        self.width.setObjectName(u"width")

        self.horizontalLayout_3.addWidget(self.width)

        self.label_5 = QLabel(Raw_info)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(Raw_info)
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

        self.verticalLayout_3.addWidget(self.groupBox)

        self.checkBox = QCheckBox(Raw_info)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.groupBox_3 = QGroupBox(Raw_info)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.wb = QComboBox(self.groupBox_3)
        self.wb.addItem("")
        self.wb.addItem("")
        self.wb.setObjectName(u"wb")

        self.horizontalLayout_6.addWidget(self.wb)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.gamma = QLineEdit(self.groupBox_3)
        self.gamma.setObjectName(u"gamma")
        self.gamma.setFrame(True)
        self.gamma.setEchoMode(QLineEdit.EchoMode.Normal)
        self.gamma.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignVCenter)
        self.gamma.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.gamma.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.gamma)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CCM = QTableView(self.groupBox_2)
        self.CCM.setObjectName(u"CCM")
        self.model = QStandardItemModel(3, 3)
        for row in range(3):
            for col in range(3):
                item = QStandardItem(f"0")
                item.setEditable(True)
                self.model.setItem(row, col, item)
        self.CCM.setModel(self.model)
        self.CCM.setObjectName(u"CCM")

        self.verticalLayout.addWidget(self.CCM)
        self.CCM.horizontalHeader().setDefaultSectionSize(self.CCM.width() // 2)  # 设置默认列宽
        self.CCM.verticalHeader().setDefaultSectionSize(self.CCM.height() // 2)  # 设置默认行高
        self.verticalLayout.addWidget(self.CCM)

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Raw_info)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Bayer = QRadioButton(self.groupBox_4)
        self.Bayer.setObjectName(u"Bayer")

        self.horizontalLayout_8.addWidget(self.Bayer)

        self.Demosica = QRadioButton(self.groupBox_4)
        self.Demosica.setObjectName(u"Demosica")

        self.horizontalLayout_8.addWidget(self.Demosica)

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.reload = QPushButton(Raw_info)
        self.reload.setObjectName(u"reload")

        self.horizontalLayout_5.addWidget(self.reload)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Raw_info)

        QMetaObject.connectSlotsByName(Raw_info)

    # setupUi

    def retranslateUi(self, Raw_info):
        Raw_info.setWindowTitle(QCoreApplication.translate("Raw_info", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Raw_info", u"Bit Depth", None))
        self.bit_depth.setText("")
        self.label.setText(QCoreApplication.translate("Raw_info", u"Height", None))
        self.height.setText("")
        self.label_4.setText(QCoreApplication.translate("Raw_info", u"pixels", None))
        self.label_2.setText(QCoreApplication.translate("Raw_info", u"width  ", None))
        self.width.setText("")
        self.label_5.setText(QCoreApplication.translate("Raw_info", u"pixels", None))
        self.groupBox.setTitle(QCoreApplication.translate("Raw_info", u"Raw Pattern", None))
        self.rg.setText(QCoreApplication.translate("Raw_info", u"RG", None))
        self.bg.setText(QCoreApplication.translate("Raw_info", u"BG", None))
        self.gb.setText(QCoreApplication.translate("Raw_info", u"GB", None))
        self.gr.setText(QCoreApplication.translate("Raw_info", u"GR", None))
        self.checkBox.setText(QCoreApplication.translate("Raw_info", u"Bigger-endian byte order", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Raw_info", u"\u57fa\u672c\u5904\u7406", None))
        self.label_6.setText(QCoreApplication.translate("Raw_info", u"white balance", None))
        self.wb.setItemText(0, QCoreApplication.translate("Raw_info", u"GrayworldWB", None))
        self.wb.setItemText(1, QCoreApplication.translate("Raw_info", u"SimpleWB", None))

        self.label_7.setText(QCoreApplication.translate("Raw_info", u"gamma", None))
        self.gamma.setText(QCoreApplication.translate("Raw_info", u"1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Raw_info", u"CCM", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Raw_info", u"View Mode", None))
        self.Bayer.setText(QCoreApplication.translate("Raw_info", u"Bayer", None))
        self.Demosica.setText(QCoreApplication.translate("Raw_info", u"Demosica", None))
        self.reload.setText(QCoreApplication.translate("Raw_info", u"reload", None))
    # retranslateUi
