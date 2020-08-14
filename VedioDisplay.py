from time import ctime, sleep
import time
from typing import Pattern, Tuple
import cv2
import os
import threading

from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QHeaderView, QDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtGui import  QStandardItemModel,QStandardItem

import gui.PATH as PATH
from myvideo import detect
from gui.Ui_help import Ui_Dialog
from gui.Ui_RoadChoose import Ui_Dialog_chooseRoad


class helpdialog(QDialog):
    """帮助手册子菜单实现类"""
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class roadchoosedialog(QDialog):
    """设置路口名"""
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog_chooseRoad()
        self.ui.setupUi(self)
        self.ui.chooseRoad.addItem('所有路口')
        self.ui.chooseRoad.addItems(PATH.get_allroads())
        self.ui.chooseRoad.currentIndexChanged.connect(self.set_roadinfo)
        
    def set_roadinfo(self):
        if self.ui.chooseRoad.currentText() == "所有路口":
            pass
        else:
            print("1")
            try:
                self.ui.choose_time.addItems(PATH.get_chosed_roadinfo(self.ui.chooseRoad.currentText()))
            except:
                dig = QMessageBox.information(self, "提示", "当前路口没有处理视频！", QMessageBox.Yes)



class Worker(QObject):
    def __init__(self, in_name, out_name):
        super().__init__()
        self.fileName = in_name
        self.video_outname = out_name

    finished = pyqtSignal()
    show_processed_vedio = pyqtSignal()

    @pyqtSlot()
    def work(self): # A slot takes no params
        print("检测开始")
        detect(self.fileName,self.video_outname, self.light_Pos)
        self.finished.emit()
        self.show_processed_vedio.emit()
        print("检测结束")


class Display:
    def __init__(self, mainWnd):
        self.mainWnd = mainWnd
        self.ui = mainWnd.ui
        self.stop = False
        
        #界面所有按钮的初始化
        self.ui.Open.setEnabled(True)
        self.ui.Close.setEnabled(False)
        self.ui.Api_button.setEnabled(False)
        self.ui.Continue.setEnabled(False)
        self.ui.Button_GetPos.setEnabled(False)

        # 信号槽设置
        self.ui.Open.clicked.connect(self.Open)
        self.ui.Close.clicked.connect(self.Close)
        self.ui.Continue.clicked.connect(self.Stop)
        self.ui.Api_button.clicked.connect(self.Api_button)

        #菜单栏设置
        self.ui.actionDelet_existdata.triggered.connect(self.Delet_exist_data)
        self.ui.delete_cache.triggered.connect(self.Delet_cache_data)
        self.ui.actionHelp.triggered.connect(self.helpdig)
        self.ui.action_SetRoad.triggered.connect(self.set_road)
        self.ui.action_choose_road.triggered.connect(self.choose_road)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

        #创建用于运行detect的线程
        self.thread = QThread()  # no parent!


    def Open(self):
        """打开视频原文件按钮响应函数"""
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.avi')
        self.video_outname = ''
        
        if self.fileName is None or '.avi' not in self.fileName:
            return
        if 'out' not in self.video_outname: 
            VedioDate = time.ctime(os.path.getctime(self.fileName))
            VedioDate = VedioDate.replace(' ', "_").replace(':', '_').replace('__', '_')
            PATH.setValue('CVedioDate', VedioDate)
            self.video_outname = PATH.run_a_red_light_vedio_path + PATH.get_roadname() + PATH.get_VedioDate()

        # 创建视频显示线程
        self.cap = cv2.VideoCapture(self.fileName)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        th = threading.Thread(target=self.Display)
        th.start()


    def Stop(self):
        """暂停按钮响应函数"""
        self.stop = not self.stop


    def Close(self):
        """关闭按钮响应函数"""
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()
        sleep(0.1)
        self.thread.quit()


    def Display(self):
        """视频展示函数"""
        if self.mainWnd.checkstats is True:
            self.stop = False

        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)
        self.ui.Continue.setEnabled(True)
        self.ui.Api_button.setEnabled(True)
        self.ui.Button_GetPos.setEnabled(True)

        while self.cap.isOpened():
            if not self.stop:
                success, frame = self.cap.read()
                # RGB转BGR
                try:
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    self.ui.DisplayLabel.setPixmap(QPixmap.fromImage(img))
                    self.ui.DisplayLabel.setScaledContents(True)
                    cv2.waitKey(int(1000 / self.frameRate))
                except:
                    self.stopEvent.set()
            
            # 判断关闭事件是否已触发
            if self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DisplayLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                break
        self.cap.release() #关闭打开的视频
        print("视频播放线程结束")


    def Api_button(self):
        """检测API接口"""
        print(self.fileName)
        print(self.video_outname)
        PATH.cheakFolders()
        
        tuple_Pos = self.mainWnd.x, self.mainWnd.y
        print(tuple_Pos)
        print(tuple_Pos[0])
        self.worker = Worker(self.fileName, self.video_outname)
        self.worker.finished.connect(self.thread.quit)
        self.thread.started.connect(self.worker.work)
        self.worker.show_processed_vedio.connect(self.show_processed_vedio)

        self.stopEvent.set()
        print("正在关原视频")
        sleep(1)
        self.ui.DisplayLabel.setText( " "*30 +"正在检测视频，请勿退出系统")
        print("Qthread开始")
        self.worker.moveToThread(self.thread)
        self.thread.start()


    def show_processed_vedio(self):
        """显示detected视频以及违法信息"""
        #违章表格初始化
        with open(PATH.run_a_red_lightpath,  encoding='UTF-8') as fp:
            data =[]
            data = fp.readlines()
            row_lenth = len(data)
        self.model=QStandardItemModel()#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['车牌号码','违章类型'])
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in range(row_lenth):
            plate_number, ilegal_type = data[row].split(' ')   
            ilegal_type = ilegal_type.replace('\n','')
            i = QStandardItem(plate_number)
            j = QStandardItem(ilegal_type)
            self.model.setItem(row,0,i)
            self.model.setItem(row,1,j)

        # 创建视频显示线程
        self.ui.tableView.setModel(self.model)
        print("开始播放")
        self.cap = cv2.VideoCapture(self.video_outname)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        th1 = threading.Thread(target=self.Display)
        th1.start()


    def Delet_exist_data(self):
        """删除所有现存的detect_result数据以便重新开始"""
        res1 = QMessageBox.warning(self.mainWnd, "警告", "请确保已保存好了必要的信息，确定继续吗？", QMessageBox.Yes | QMessageBox.No)
        if (QMessageBox.No == res1):
            return
        try:
            #删除txt文件内容
            open(PATH.run_a_red_lightpath, 'w').close()
            open(PATH.resultpath, 'w').close()

            #删除img文件
            img_path = [PATH.caroutputpath, PATH.run_a_red_light_img_path, PATH.trafficoutputpath]
            for i in range(0,3):
                os.chdir(img_path[i]) 
                fileList = list(os.listdir()) 
                for file in fileList: 
                    os.remove(file) 
        
        except PermissionError:
            res2 = QMessageBox.information(self.mainWnd, "提示", "您正在使用该文件，请关闭后再执行", QMessageBox.Yes)
            return

        print("delete successfully")
        res2 = QMessageBox.information(self.mainWnd, "提示", "删除数据成功！", QMessageBox.Yes)
    

    def Delet_cache_data(self):
        """只删除缓存数据"""
        res1 = QMessageBox.warning(self.mainWnd, "警告", "请确保已保存好了必要的信息，确定继续吗？", QMessageBox.Yes | QMessageBox.No)
        if (QMessageBox.No == res1):
            return
        try:
            #删除img文件
            img_path = [PATH.caroutputpath, PATH.trafficoutputpath]
            for i in range(0,2):
                os.chdir(img_path[i]) 
                fileList = list(os.listdir()) 
                for file in fileList: 
                    os.remove(file) 
        except PermissionError:
            res2 = QMessageBox.information(self.mainWnd, "提示", "您正在使用该文件，请关闭后再执行", QMessageBox.Yes)
            return

        print("delete successfully")
        res2 = QMessageBox.information(self.mainWnd, "提示", "删除img缓存成功！", QMessageBox.Yes)


    def helpdig(self):
        """显示帮助文档"""
        self.hlpdig = helpdialog()
        self.hlpdig.show()
        

    def set_road(self):
        """路口名称设置"""
        text, okPressed = QInputDialog.getText(self.mainWnd, "提示","输入当前路口：", QLineEdit.Normal, "")
        if okPressed and text != '':
            print("当前检测路口为:" + text)
            PATH.setValue('RoadName', text)
            self.mainWnd.ui.label_road_text.setText(PATH.get_roadname())
        else:
            self.mainWnd.ui.label_road_text.setText(PATH.get_roadname())
        

    def choose_road(self):
        """选择已经处理的视频"""
        self.choosedig = roadchoosedialog()
        self.choosedig.show()