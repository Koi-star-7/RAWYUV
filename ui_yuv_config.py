# 打开yuv图时的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yuv_config.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_YUV_Config(object):
    def setupUi(self, yuv_config):
        if not yuv_config.objectName():
            yuv_config.setObjectName(u"yuv_config")
        yuv_config.resize(240, 321)
        self.verticalLayout = QVBoxLayout(yuv_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(yuv_config)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.width = QLineEdit(yuv_config)
        self.width.setObjectName(u"width")

        self.horizontalLayout.addWidget(self.width)

        self.label_3 = QLabel(yuv_config)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(yuv_config)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.height = QLineEdit(yuv_config)
        self.height.setObjectName(u"height")

        self.horizontalLayout_2.addWidget(self.height)

        self.label_4 = QLabel(yuv_config)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(yuv_config)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox = QComboBox(yuv_config)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(yuv_config)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(yuv_config)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(yuv_config)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox = QCheckBox(yuv_config)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.buttonBox = QDialogButtonBox(yuv_config)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(yuv_config)
        self.buttonBox.accepted.connect(yuv_config.accept)
        self.buttonBox.rejected.connect(yuv_config.reject)

        QMetaObject.connectSlotsByName(yuv_config)
    # setupUi

    def retranslateUi(self, yuv_config):
        yuv_config.setWindowTitle(QCoreApplication.translate("yuv_config", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("yuv_config", u"width", None))
        self.label_3.setText(QCoreApplication.translate("yuv_config", u"pixels", None))
        self.label_2.setText(QCoreApplication.translate("yuv_config", u"height", None))
        self.label_4.setText(QCoreApplication.translate("yuv_config", u"pixels", None))
        self.label_5.setText(QCoreApplication.translate("yuv_config", u"pattern", None))
        self.label_6.setText(QCoreApplication.translate("yuv_config", u"standard ", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("yuv_config", u"BT.601", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("yuv_config", u"BT.709", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("yuv_config", u"BT.2020", None))

        self.checkBox.setText(QCoreApplication.translate("yuv_config", u"TV range", None))
    # retranslateUi

