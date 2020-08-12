# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\DeepLearning\mytraffic_cv\gui\illegal_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogillgal(object):
    def setupUi(self, dialogillgal):
        dialogillgal.setObjectName("dialogillgal")
        dialogillgal.resize(835, 512)
        dialogillgal.setMinimumSize(QtCore.QSize(835, 502))
        dialogillgal.setMaximumSize(QtCore.QSize(835, 512))
        self.line = QtWidgets.QFrame(dialogillgal)
        self.line.setGeometry(QtCore.QRect(650, 0, 21, 511))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(dialogillgal)
        self.label_2.setGeometry(QtCore.QRect(690, 10, 71, 41))
        self.label_2.setObjectName("label_2")
        self.plate_number = QtWidgets.QLabel(dialogillgal)
        self.plate_number.setGeometry(QtCore.QRect(710, 50, 101, 21))
        self.plate_number.setObjectName("plate_number")
        self.label_4 = QtWidgets.QLabel(dialogillgal)
        self.label_4.setGeometry(QtCore.QRect(690, 110, 71, 41))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.illegal_type = QtWidgets.QLabel(dialogillgal)
        self.illegal_type.setGeometry(QtCore.QRect(710, 150, 101, 21))
        self.illegal_type.setObjectName("illegal_type")
        self.verticalLayoutWidget = QtWidgets.QWidget(dialogillgal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(531, 321))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.before = QtWidgets.QPushButton(dialogillgal)
        self.before.setGeometry(QtCore.QRect(700, 250, 101, 51))
        self.before.setObjectName("before")
        self.next = QtWidgets.QPushButton(dialogillgal)
        self.next.setGeometry(QtCore.QRect(700, 330, 101, 51))
        self.next.setObjectName("next")
        self.line_2 = QtWidgets.QFrame(dialogillgal)
        self.line_2.setGeometry(QtCore.QRect(660, 90, 221, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(dialogillgal)
        self.line_3.setGeometry(QtCore.QRect(660, 200, 211, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.delete_info = QtWidgets.QPushButton(dialogillgal)
        self.delete_info.setGeometry(QtCore.QRect(700, 410, 101, 51))
        self.delete_info.setObjectName("delete_info")

        self.retranslateUi(dialogillgal)
        QtCore.QMetaObject.connectSlotsByName(dialogillgal)

    def retranslateUi(self, dialogillgal):
        _translate = QtCore.QCoreApplication.translate
        dialogillgal.setWindowTitle(_translate("dialogillgal", "查看违法帧"))
        self.label_2.setText(_translate("dialogillgal", "车牌号码："))
        self.plate_number.setText(_translate("dialogillgal", " "))
        self.label_4.setText(_translate("dialogillgal", "违法类别："))
        self.illegal_type.setText(_translate("dialogillgal", " "))
        self.label.setText(_translate("dialogillgal", "                                 点击下一张开始展示"))
        self.before.setText(_translate("dialogillgal", "上一张"))
        self.next.setText(_translate("dialogillgal", "下一张"))
        self.delete_info.setText(_translate("dialogillgal", "删除信息"))

