# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\mytraffic_cv\gui\Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 885)
        MainWindow.setMinimumSize(QtCore.QSize(1154, 885))
        MainWindow.setMaximumSize(QtCore.QSize(1154, 885))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(780, 0, 51, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.DisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.DisplayLabel.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.DisplayLabel.setMinimumSize(QtCore.QSize(711, 431))
        self.DisplayLabel.setMaximumSize(QtCore.QSize(801, 501))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.DisplayLabel.setFont(font)
        self.DisplayLabel.setTextFormat(QtCore.Qt.AutoText)
        self.DisplayLabel.setObjectName("DisplayLabel")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(1, 536, 801, 291))
        self.tableView.setMinimumSize(QtCore.QSize(721, 281))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSortIndicatorShown(False)
        self.label_road = QtWidgets.QLabel(self.centralwidget)
        self.label_road.setGeometry(QtCore.QRect(810, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.label_road.setFont(font)
        self.label_road.setObjectName("label_road")
        self.label_road_text = QtWidgets.QLabel(self.centralwidget)
        self.label_road_text.setGeometry(QtCore.QRect(940, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.label_road_text.setFont(font)
        self.label_road_text.setText("")
        self.label_road_text.setObjectName("label_road_text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, -25, 1171, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(810, 100, 341, 251))
        self.calendarWidget.setMinimumSize(QtCore.QSize(311, 241))
        self.calendarWidget.setMaximumSize(QtCore.QSize(10000, 10000))
        self.calendarWidget.setObjectName("calendarWidget")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 810, 1171, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 500, 801, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_GetPos = QtWidgets.QPushButton(self.layoutWidget)
        self.Button_GetPos.setObjectName("Button_GetPos")
        self.horizontalLayout.addWidget(self.Button_GetPos)
        self.Continue = QtWidgets.QPushButton(self.layoutWidget)
        self.Continue.setObjectName("Continue")
        self.horizontalLayout.addWidget(self.Continue)
        self.Close = QtWidgets.QPushButton(self.layoutWidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout.addWidget(self.Close)
        self.Api_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Api_button.setObjectName("Api_button")
        self.horizontalLayout.addWidget(self.Api_button)
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(910, 380, 141, 71))
        self.Open.setMinimumSize(QtCore.QSize(141, 71))
        self.Open.setMaximumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.Button_imgout = QtWidgets.QPushButton(self.centralwidget)
        self.Button_imgout.setGeometry(QtCore.QRect(910, 500, 141, 71))
        self.Button_imgout.setMinimumSize(QtCore.QSize(141, 71))
        self.Button_imgout.setMaximumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.Button_imgout.setFont(font)
        self.Button_imgout.setObjectName("Button_imgout")
        self.Button_infoout = QtWidgets.QPushButton(self.centralwidget)
        self.Button_infoout.setGeometry(QtCore.QRect(910, 620, 141, 71))
        self.Button_infoout.setMinimumSize(QtCore.QSize(141, 71))
        self.Button_infoout.setMaximumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.Button_infoout.setFont(font)
        self.Button_infoout.setObjectName("Button_infoout")
        self.Button_quit = QtWidgets.QPushButton(self.centralwidget)
        self.Button_quit.setGeometry(QtCore.QRect(910, 740, 141, 71))
        self.Button_quit.setMinimumSize(QtCore.QSize(141, 71))
        self.Button_quit.setMaximumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.Button_quit.setFont(font)
        self.Button_quit.setObjectName("Button_quit")
        self.label_light = QtWidgets.QLabel(self.centralwidget)
        self.label_light.setGeometry(QtCore.QRect(810, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.label_light.setFont(font)
        self.label_light.setObjectName("label_light")
        self.label_ligh_text = QtWidgets.QLabel(self.centralwidget)
        self.label_ligh_text.setGeometry(QtCore.QRect(980, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.label_ligh_text.setFont(font)
        self.label_ligh_text.setText("")
        self.label_ligh_text.setObjectName("label_ligh_text")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(810, 29, 351, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(807, 79, 361, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_helper = QtWidgets.QMenu(self.menubar)
        self.menu_helper.setObjectName("menu_helper")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDelet_existdata = QtWidgets.QAction(MainWindow)
        self.actionDelet_existdata.setObjectName("actionDelet_existdata")
        self.delete_cache = QtWidgets.QAction(MainWindow)
        self.delete_cache.setObjectName("delete_cache")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionZidonghua = QtWidgets.QAction(MainWindow)
        self.actionZidonghua.setObjectName("actionZidonghua")
        self.action_choose_road = QtWidgets.QAction(MainWindow)
        self.action_choose_road.setObjectName("action_choose_road")
        self.action_SetRoad = QtWidgets.QAction(MainWindow)
        self.action_SetRoad.setObjectName("action_SetRoad")
        self.menu.addAction(self.action_SetRoad)
        self.menu.addSeparator()
        self.menu.addAction(self.actionDelet_existdata)
        self.menu.addAction(self.delete_cache)
        self.menu.addSeparator()
        self.menu.addAction(self.action_choose_road)
        self.menu_helper.addAction(self.actionHelp)
        self.menu_2.addAction(self.actionZidonghua)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_helper.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.Button_quit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "道路违法检测系统"))
        self.DisplayLabel.setText(_translate("MainWindow", "                                                 视频播放区域"))
        self.label_road.setText(_translate("MainWindow", "监控路口："))
        self.Button_GetPos.setText(_translate("MainWindow", "参数配置"))
        self.Continue.setText(_translate("MainWindow", "暂停/继续"))
        self.Close.setText(_translate("MainWindow", "关闭"))
        self.Api_button.setText(_translate("MainWindow", "检测"))
        self.Open.setText(_translate("MainWindow", "导入原视频文件"))
        self.Button_imgout.setText(_translate("MainWindow", "查看违章帧"))
        self.Button_infoout.setText(_translate("MainWindow", "导出违章文本信息"))
        self.Button_quit.setText(_translate("MainWindow", "退出系统"))
        self.label_light.setText(_translate("MainWindow", "红绿灯参数："))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_helper.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "自动化"))
        self.actionDelet_existdata.setText(_translate("MainWindow", "清除数据（包括违法记录）"))
        self.delete_cache.setText(_translate("MainWindow", "只清理缓存"))
        self.actionHelp.setText(_translate("MainWindow", "查看使用手册"))
        self.actionZidonghua.setText(_translate("MainWindow", "自动化检测"))
        self.action_choose_road.setText(_translate("MainWindow", "查看已处理视频"))
        self.action_SetRoad.setText(_translate("MainWindow", "设置路口"))

