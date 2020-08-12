#通用全局变量管理文件

import os
#通用路径设置
ProjectPath = os.path.dirname(os.path.dirname(__file__)) + '\\'
DeskTop_path = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
Gui_path = ProjectPath + "mytraffic_cv\\Main_Gui.py"

trafficoutputpath=ProjectPath + "mytraffic_cv\\detect_result\\traffic\\"
caroutputpath=ProjectPath + "mytraffic_cv\\detect_result\\car\\"
resultpath=ProjectPath + "mytraffic_cv\\detect_result\\result.txt"
run_a_red_lightpath=ProjectPath + "mytraffic_cv\\detect_result\\illegal_act\\illegal_car_info.txt"
run_a_red_light_img_path=ProjectPath + "mytraffic_cv\\detect_result\\illegal_act\\illegal_car_img\\"
model_ocr_plate_all_w_rnn_2=ProjectPath+"mytraffic_cv\\model\\ocr_plate_all_w_rnn_2.h5"
caridpath=ProjectPath + "mytraffic_cv\\detect_result\\carid\\"

model_cascade=ProjectPath+"mytraffic_cv\\model\\cascade.xml"
model_cascade_lbp=ProjectPath+"mytraffic_cv\\model\\cascade_lbp.xml"
model_cascade_lbp=ProjectPath+"mytraffic_cv\\model\\cascade_lbp.h5"
model_char_judgement=ProjectPath+"mytraffic_cv\\model\\char_judgement.h5"
model_char_judgement1=ProjectPath+"mytraffic_cv\\model\\char_judgement1.h5"
model_char_rec=ProjectPath+"mytraffic_cv\\model\\char_rec.h5"
model_lpr=ProjectPath+"mytraffic_cv\\model\\lpr.h5"
model_MobileNetSSD_test=ProjectPath+"mytraffic_cv\\model\\MobileNetSSD_test.prototxt"
model_model12=ProjectPath+"mytraffic_cv\\model\\model12.h5"
model_ocr_plate_all_gru=ProjectPath+"mytraffic_cv\\model\\ocr_plate_all_gru.h5"
model_plate_type=ProjectPath+"mytraffic_cv\\model\\plate_type.h5"




"""设置通用全局变量"""
global _global_dict
_global_dict = {}

def setValue(name:str, value:str):
    _global_dict[name] = value

def getValue(name:str, defvalue = None) -> str:
    try:
        return _global_dict[name]
    except KeyError:
        return defvalue