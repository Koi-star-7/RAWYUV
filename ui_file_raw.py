# 点击转换按钮后的UI界面

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_raw.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_file_save(object):
    def setupUi(self, file_save):
        if not file_save.objectName():
            file_save.setObjectName(u"file_save")
        file_save.resize(320, 240)
        self.verticalLayout_3 = QVBoxLayout(file_save)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.v1 = QVBoxLayout()
        self.v1.setObjectName(u"v1")
        self.h2 = QHBoxLayout()
        self.h2.setObjectName(u"h2")
        self.label = QLabel(file_save)
        self.label.setObjectName(u"label")

        self.h2.addWidget(self.label)

        self.fiepath = QLineEdit(file_save)
        self.fiepath.setObjectName(u"fiepath")

        self.h2.addWidget(self.fiepath)

        self.filepath_choose = QPushButton(file_save)
        self.filepath_choose.setObjectName(u"filepath_choose")

        self.h2.addWidget(self.filepath_choose)


        self.v1.addLayout(self.h2)

        self.h1 = QHBoxLayout()
        self.h1.setObjectName(u"h1")
        self.label_2 = QLabel(file_save)
        self.label_2.setObjectName(u"label_2")

        self.h1.addWidget(self.label_2)

        self.filename = QLineEdit(file_save)
        self.filename.setObjectName(u"filename")

        self.h1.addWidget(self.filename)

        self.type = QComboBox(file_save)
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.setObjectName(u"type")

        self.h1.addWidget(self.type)


        self.v1.addLayout(self.h1)


        self.verticalLayout_3.addLayout(self.v1)

        self.buttonBox = QDialogButtonBox(file_save)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(file_save)
        self.buttonBox.accepted.connect(file_save.accept)
        self.buttonBox.rejected.connect(file_save.reject)

        QMetaObject.connectSlotsByName(file_save)
    # setupUi

    def retranslateUi(self, file_save):
        file_save.setWindowTitle(QCoreApplication.translate("file_save", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("file_save", u"filepath", None))
        self.filepath_choose.setText(QCoreApplication.translate("file_save", u"...", None))
        self.label_2.setText(QCoreApplication.translate("file_save", u"filename", None))
        self.type.setItemText(0, QCoreApplication.translate("file_save", u".raw", None))
        self.type.setItemText(1, QCoreApplication.translate("file_save", u".yuv", None))
        self.type.setItemText(2, QCoreApplication.translate("file_save", u".bmp", None))
        self.type.setItemText(3, QCoreApplication.translate("file_save", u".jpg", None))
        self.type.setItemText(4, QCoreApplication.translate("file_save", u".png", None))

    # retranslateUi