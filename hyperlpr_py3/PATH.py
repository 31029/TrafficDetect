import os
ProjectPath = os.path.dirname(os.path.dirname(__file__)) + '\\'
DeskTop_path = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'


trafficoutputpath=ProjectPath + "mytraffic_cv\\detect_result\\traffic\\"
caroutputpath=ProjectPath + "mytraffic_cv\\detect_result\\car\\"
resultpath=ProjectPath + "mytraffic_cv\\detect_result\\result.txt"
run_a_red_lightpath=ProjectPath + "mytraffic_cv\\detect_result\\illegal_act\\illegal_car_info.txt"
run_a_red_light_img_path=ProjectPath + "mytraffic_cv\\detect_result\\illegal_act\\illegal_car_img\\"

