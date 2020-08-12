import os
ProjectPath = os.path.dirname(os.path.dirname(__file__)) + '\\'
DeskTop_path = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'

trafficoutputpath=ProjectPath + "detect_result\\traffic\\"
caroutputpath=ProjectPath + "detect_result\\car\\"
resultpath=ProjectPath + "detect_result\\result.txt"
run_a_red_lightpath=ProjectPath + "detect_result\\illegal_act\\illegal_car_info.txt"
run_a_red_light_img_path=ProjectPath + "detect_result\\illegal_act\\illegal_car_img\\"
