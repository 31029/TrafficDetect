import sys, os 
import gui.PATH as PATH
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
        if PATH.bool_alltimes is True:
            self.imgpaths = []
            self.imgs_dict = PATH.get_road_imgspaths(PATH.get_roadname())
            for img_info in self.imgs_dict.keys():
                Road, Date, img = img_info.split(':')
                self.imgnames_list.append(img)
                self.imgpaths.append(self.imgs_dict[img_info])
        else:
            self.imgnames_list = list(os.listdir(PATH.run_a_red_light_img_path()))
        
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
        else:
            try:
                del_name = self.imgnames_list.pop(self.current_img_index)
                del_name = del_name[0:7]
                if PATH.bool_alltimes is True:  
                    os.remove(self.imgpaths[self.current_img_index])
                    _ = self.imgpaths[self.current_img_index].split("\\")
                    txtpath = PATH.Road_ROOTpath() + _[4] + "\\illegal_car_info.txt"
                else:
                    os.remove(PATH.run_a_red_light_img_path() + del_name)
                    txtpath = PATH.run_a_red_lightpath()

                with open(txtpath, 'r', encoding='UTF-8') as fp:
                    lines = fp.readlines()
                    for i in range(len(lines)):
                        if del_name in lines[i]:
                            lines[i] = ''
                    fp.close()
                with open(txtpath, 'w', encoding='UTF-8') as fp:
                    fp.writelines(lines)
            except:
                box = QMessageBox.warning(self.wnd, "提示", "删除错误", QMessageBox.Yes)
            box = QMessageBox.warning(self.wnd, "提示", "删除成功！", QMessageBox.Yes)
            self.current_img_index = 0
            self.display_info()


    def display_info(self):
        """展示违法信息"""
        try:
            n, m = self.imgnames_list[self.current_img_index].split('_')
            m = str(m).replace('.jpg', '')
            self.ui.plate_number.setText(n)
            self.ui.illegal_type.setText(m)
            if PATH.bool_alltimes is True:
                self.ui.label.setPixmap(QPixmap(self.imgpaths[self.current_img_index]))
            else:
                self.ui.label.setPixmap(QPixmap(PATH.run_a_red_light_img_path() + self.imgnames_list[self.current_img_index]))
            self.ui.label.setScaledContents(True)
        except:
            box = QMessageBox.warning(self.wnd, "提示", "库存为空", QMessageBox.Yes)