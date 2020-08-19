# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\mytraffic_cv\gui\RoadChoose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_chooseRoad(object):
    def setupUi(self, Dialog_chooseRoad):
        Dialog_chooseRoad.setObjectName("Dialog_chooseRoad")
        Dialog_chooseRoad.resize(349, 171)
        Dialog_chooseRoad.setMinimumSize(QtCore.QSize(349, 171))
        Dialog_chooseRoad.setMaximumSize(QtCore.QSize(349, 171))
        self.formLayoutWidget = QtWidgets.QWidget(Dialog_chooseRoad)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 341, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.chooseRoad = QtWidgets.QComboBox(self.formLayoutWidget)
        self.chooseRoad.setObjectName("chooseRoad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chooseRoad)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label)
        self.choose_time = QtWidgets.QComboBox(self.formLayoutWidget)
        self.choose_time.setObjectName("choose_time")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.choose_time)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog_chooseRoad)
        self.pushButton_ok.setGeometry(QtCore.QRect(150, 130, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_quit = QtWidgets.QPushButton(Dialog_chooseRoad)
        self.pushButton_quit.setGeometry(QtCore.QRect(250, 130, 93, 28))
        self.pushButton_quit.setObjectName("pushButton_quit")

        self.retranslateUi(Dialog_chooseRoad)
        self.pushButton_quit.clicked.connect(Dialog_chooseRoad.close)
        self.pushButton_ok.clicked.connect(Dialog_chooseRoad.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog_chooseRoad)

    def retranslateUi(self, Dialog_chooseRoad):
        _translate = QtCore.QCoreApplication.translate
        Dialog_chooseRoad.setWindowTitle(_translate("Dialog_chooseRoad", "选择路口对话框"))
        self.label_2.setText(_translate("Dialog_chooseRoad", "选择路口："))
        self.label.setText(_translate("Dialog_chooseRoad", "选择时间段："))
        self.pushButton_ok.setText(_translate("Dialog_chooseRoad", "确定"))
        self.pushButton_quit.setText(_translate("Dialog_chooseRoad", "取消"))

