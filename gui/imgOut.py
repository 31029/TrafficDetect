from os.path import split
import sys, os

from gui.PATH import run_a_red_light_img_path, run_a_red_lightpath
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

class imgOut:
    def __init__(self, wnd):
        self.ui = wnd.ui
        self.wnd = wnd
        self.current_img_index = 0
        self.imgnames_list = []
        self.ui.before.setEnabled(False)
        self.ui.delete_info.setEnabled(False)

        self.ui.before.clicked.connect(self.before_img)
        self.ui.next.clicked.connect(self.next_img)
        self.ui.delete_info.clicked.connect(self.delet_info)


    def img_init(self):
        """初始化img列表"""
        self.imgnames_list = list(os.listdir(run_a_red_light_img_path))
        if len(self.imgnames_list) != 0:
            self.display_info()
            self.ui.before.setEnabled(True)
            self.ui.delete_info.setEnabled(True)
        else:
            box = QMessageBox.warning(self.wnd, "提示", "库存为空", QMessageBox.Yes)


    def before_img(self):
        """上一张图片"""
        if self.current_img_index == 0:
            return
        else:
            self.current_img_index = self.current_img_index - 1
        self.display_info()
        

    def next_img(self):
        """下一张图片"""
        if len(self.imgnames_list) == 0:
            self.img_init()
        else:
            self.ui.before.setEnabled(True)
            self.ui.delete_info.setEnabled(True)
            if self.current_img_index == len(self.imgnames_list)-1:
                self.current_img_index = 0
            else:
                self.current_img_index = self.current_img_index + 1
            self.display_info()


    def delet_info(self):
        """删除展示车辆的违法信息"""
        box = QMessageBox.warning(self.wnd, "提示", "确定删除该车辆的违法信息？", QMessageBox.Yes | QMessageBox.No)
        if box == QMessageBox.No:
            return

        del_name = self.imgnames_list.pop(self.current_img_index)
        del_name = del_name[0:7]
        a = []
        a.append('del:'+del_name)
        
        os.remove(run_a_red_light_img_path + del_name)
        with open(run_a_red_lightpath, 'r', encoding='UTF-8') as fp:
            lines = fp.readlines()
            for i in range(len(lines)):
                if del_name in lines[i]:
                     lines[i] = ''
            fp.close()
        with open(run_a_red_lightpath, 'w', encoding='UTF-8') as fp:
            fp.writelines(lines)

        self.current_img_index = 0
        self.display_info()


    def display_info(self):
        """展示违法信息"""
        try:
            n, m = self.imgnames_list[self.current_img_index].split('_')
            m = str(m).replace('.jpg', '')
            self.ui.plate_number.setText(n)
            self.ui.illegal_type.setText(m)
            self.ui.label.setPixmap(QPixmap(run_a_red_light_img_path + self.imgnames_list[self.current_img_index]))
            self.ui.label.setScaledContents(True)
        except:
            box = QMessageBox.warning(self.wnd, "提示", "库存为空", QMessageBox.Yes)