import os
import datetime
from typing import List

#通用全局变量和函数管理文件
"""
    通用全局变量：
    CVedioDate: 当前录像的时间 -> str
    RoadName：当前监测路口名 -> str 

    all_roads: 所有检测路口名 -> List
"""
#全局字典
global _global_dict
global bool_alltimes
global bool_allroads
bool_allroads = False
bool_alltimes = False
_global_dict = {}
_global_dict['default_road'] = "测试路口"
_global_dict['default_date'] = datetime.datetime.now().strftime('%Y-%m-%d')

#通用路径设置
ProjectPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DeskTop_path = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
Gui_path = ProjectPath + "mytraffic_cv\\Main_Gui.py"

#结果存放路径
detect_result_path = ProjectPath + "mytraffic_cv\\detect_result\\"
trafficoutputpath  =  detect_result_path + "cache\\traffic\\"
caroutputpath  =  detect_result_path + "cache\\car\\"
resultpath = detect_result_path + "cache\\result.txt"

model_ocr_plate_all_w_rnn_2 = ProjectPath + "mytraffic_cv\\model\\ocr_plate_all_w_rnn_2.h5"
caridpath=ProjectPath + "mytraffic_cv\\detect_result\\cache\\carid\\"

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


#全局函数
def setValue(name:str, value:str):
    print("设置全局变量： "+ name + ":" + value)
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

#文件夹操作API
for root, subdirs, files in os.walk(ProjectPath + "mytraffic_cv\\detect_result"):
    _global_dict['all_roads'] = subdirs
    _global_dict['all_roads'].remove('cache')
    break


##变化的存储路径的默认值
def Road_ROOTpath():
    return detect_result_path + get_roadname() + "\\"
    
def Road_illegal_Info():
    return  Road_ROOTpath() + get_VedioDate()

def run_a_red_light_vedio_path():
    a = Road_illegal_Info() + "Vedio_out.avi"
    return a

def run_a_red_light_img_path():
    a = Road_illegal_Info() 
    return a + "\\illegal_imgs\\"

def run_a_red_lightpath():
    a = Road_illegal_Info()
    return a + "\\illegal_car_info.txt"

def infomation_path():
    a = Road_illegal_Info()
    return a + "\\infomation.png"


##复杂操作
def get_allroads() -> List:
    """获取所有路口名"""
    try:
        return _global_dict['all_roads']
    except KeyError:
        return []
        
def get_chosed_roadinfo(Roadname:str) -> List:
    """获取当前检测路口的所有时间段的名称，用于addItems"""
    for root, subdirs, files in os.walk(ProjectPath + "mytraffic_cv\\detect_result\\" + Roadname):
        _global_dict['chosed_roadinfo'] = subdirs
        return subdirs

def get_road_imgspaths(Roadname:str) -> dict:
    """获取当前检测路口的所有时间段内imgs的路径"""
    img_paths = {}
    roadinfo_list = get_chosed_roadinfo(Roadname)
    for date in roadinfo_list:
        imgs_path = detect_result_path + Roadname + "\\" + date + "\\" + "illegal_imgs" + "\\"
        imgs = list(os.listdir(imgs_path))
        for img in imgs:
            imginfo = Roadname + ':' + date + ':' + img
            img_paths[imginfo] = detect_result_path + Roadname + "\\" + date + "\\" + "illegal_imgs" + "\\" + img
    return img_paths

def get_allroads_imgs_paths() -> List:
    """返回所有路口检测的imgs结果存放的路径"""
    road_info_imgspaths = []
    all_roads_names = get_allroads()
    for roadname in all_roads_names:
        road_infos = get_chosed_roadinfo(roadname)
        for road_info in road_infos:
            road_info_imgspaths.append(detect_result_path + roadname + "\\" +  road_info + "\\")
    return road_info_imgspaths

def cheackFolders():
    """创建变化文件夹函数"""
    Road_ROOTpath = ProjectPath + "mytraffic_cv\\detect_result\\" + get_roadname() + "\\"
    Road_illegal_Info = Road_ROOTpath + get_VedioDate()
    Road_Paths = [Road_ROOTpath, Road_illegal_Info,run_a_red_light_vedio_path(), run_a_red_light_img_path()]
    for _ in Road_Paths:
        if not os.path.exists(_):
            os.mkdir(_)



