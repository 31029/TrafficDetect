## 一个实际场景下的交通路口基本信息的识别软件
该软件基于开源软件项目https://github.com/zeusees/HyperLPR 以及 https://github.com/zeusees/Mobilenet-SSD-License-Plate-Detection 开发。

支持国内蓝、黄、绿、警单行车牌的识别，车牌定位支持haar级联定位和ssd定位，车牌识别支持端到端字符识别。

支持常见的家用、商务的非机动车和机动车的识别，以及路口流量的判断。

支持红绿灯和行人的识别。

识别准确率95%，性能：普通笔记本电脑，3fps（cpu）,10fps（intel gpu）。

## 使用

直接克隆或下载项目。

项目使用pycharm，python3.7 64位版， window10 64位版开发，开发环境配置：

1. 安装anaconda3

2. pip install tensorflow
   
3. pip install keras
   
4. pip install opencv-python
   
5. 项目解压后，可以在cmd窗口，切换路径到项目路径下，执行： `python mainGUI.py`


## 贡献者
31029

