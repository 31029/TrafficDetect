import os
import datetime
from typing import List

#通用全局变量和函数管理文件
"""设置通用全局变量"""
global _global_dict
_global_dict = {}
_global_dict['default_road'] = "测试路口"
_global_dict['default_date'] = datetime.datetime.now().strftime('%Y-%m-%d')

#全局函数
def setValue(name:str, value:str):
    print("设置值： "+name, value)
    _global_dict[name] = value

def get_roadname() -> str:
    try:
        return _global_dict['RoadName']
    except KeyError:
        print("使用默认值："+_global_dict['default_road'])
        return _global_dict['default_road']

def get_VedioDate() -> str:
    try:
        return _global_dict['CVedioDate']
    except KeyError:
        print("使用默认值："+_global_dict['default_date'])
        return _global_dict['default_date']


#通用路径设置
ProjectPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DeskTop_path = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
Gui_path = ProjectPath + "mytraffic_cv\\Main_Gui.py"

#结果存放路径
detect_result_path = ProjectPath + "mytraffic_cv\\detect_result\\"
trafficoutputpath  =  detect_result_path + "cache\\traffic\\"
caroutputpath  =  detect_result_path + "cache\\car\\"
resultpath = detect_result_path + "cache\\result.txt"

#变化的存储路径的默认值
def Road_ROOTpath():
    return detect_result_path + get_roadname() + "\\"
    
def Road_illegal_Info():
    return  Road_ROOTpath() + get_VedioDate()

def run_a_red_light_vedio_path():
    a = Road_illegal_Info()
    return a

def run_a_red_light_img_path():
    a = Road_illegal_Info() 
    return a + "\\illegal_imgs\\"

def run_a_red_lightpath():
    a = Road_illegal_Info()
    return a + "\\illegal_car_info.txt"


model_ocr_plate_all_w_rnn_2 = ProjectPath + "mytraffic_cv\\model\\ocr_plate_all_w_rnn_2.h5"
caridpath=ProjectPath + "mytraffic_cv\\detect_result\\carid\\"

#模型绝对路径
model_cascade = ProjectPath + "mytraffic_cv\\model\\cascade.xml"
model_cascade_lbp = ProjectPath + "mytraffic_cv\\model\\cascade_lbp.xml"
model_cascade_lbp = ProjectPath + "mytraffic_cv\\model\\cascade_lbp.h5"
model_char_judgement  = ProjectPath + "mytraffic_cv\\model\\char_judgement.h5"
model_char_judgement1 = ProjectPath + "mytraffic_cv\\model\\char_judgement1.h5"
model_char_rec = ProjectPath + "mytraffic_cv\\model\\char_rec.h5"
model_lpr = ProjectPath + "mytraffic_cv\\model\\lpr.h5"
model_MobileNetSSD_test = ProjectPath+"mytraffic_cv\\model\\MobileNetSSD_test.prototxt"
model_model12 = ProjectPath +"mytraffic_cv\\model\\model12.h5"
model_ocr_plate_all_gru = ProjectPath + "mytraffic_cv\\model\\ocr_plate_all_gru.h5"
model_plate_type = ProjectPath + "mytraffic_cv\\model\\plate_type.h5"


#文件夹操作API
for root, subdirs, files in os.walk(ProjectPath + "mytraffic_cv\\detect_result"):
    _global_dict['all_roads'] = subdirs
    _global_dict['all_roads'].remove('cache')
    break

#def get_Road_ROOTpath() -> set:
#    return (detect_result_path + get_roadname() + "\\",detect_result_path + get_roadname() + get_VedioDate())

def get_allroads() -> List:
    try:
        return _global_dict['all_roads']
    except KeyError:
        return []

def get_chosed_roadinfo(Roadname:str) -> List:
    for root, subdirs, files in os.walk(ProjectPath + "mytraffic_cv\\detect_result\\" + Roadname):
        _global_dict['chosed_roadinfo'] = subdirs
        return subdirs

def cheackFolders():
    """创建变化文件夹函数"""
    Road_ROOTpath = ProjectPath + "mytraffic_cv\\detect_result\\" + get_roadname() + "\\"
    Road_illegal_Info = Road_ROOTpath + get_VedioDate()
    Road_Paths = [Road_ROOTpath, Road_illegal_Info,run_a_red_light_vedio_path(), run_a_red_light_img_path()]
    for _ in Road_Paths:
        if not os.path.exists(_):
            os.mkdir(_)