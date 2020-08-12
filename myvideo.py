#-------------------------------------#
#       调用摄像头检测
#-------------------------------------#
from PIL import Image,ImageDraw
import numpy as np
import cv2


def detect(video_inputpath,video_outpath, light_Pos):
    import keras
    from yolo import YOLO
    yolo = YOLO()
  
    video_inp = video_inputpath
    video_out = video_outpath 
    video_reader = cv2.VideoCapture(video_inp)
    frame_h =int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_w = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_writer = cv2.VideoWriter(video_out,
                                cv2.VideoWriter_fourcc(*'XVID'), 
                                25, 
                                (frame_w, frame_h)) 
    ref,frame=video_reader.read()
    trfn=0
    carn=0
    i=0
    lrx=920
    rrx=880
    carnums=0
    carlist=[]
    while(ref):
        # 读取某一帧
        # 格式转变，BGRtoRGB
        # i+=1
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        
        # 进行检测
        # if i% 5==0:
        r_image,i,m= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist)
        draw = ImageDraw.Draw(r_image)
        draw.line((260,850,1500,850),fill='red',width=5)
        trfn=i
        carn=m
        frame = np.array(r_image)
        #frame = np.array(yolo.detect_image(frame))

        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        video_writer.write(frame)
        ref,frame=video_reader.read()


def detect2(video_inputpath,video_outpath):
    import keras
    from yolo import YOLO
    yolo = YOLO()
  
    video_inp = video_inputpath
    video_out = video_outpath 
    video_reader = cv2.VideoCapture(video_inp)
    frame_h =int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_w = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_writer = cv2.VideoWriter(video_out,
                                cv2.VideoWriter_fourcc(*'XVID'), 
                                25, 
                                (frame_w, frame_h)) 
    ref,frame=video_reader.read()
    trfn=0
    carn=0
    i=0
    lrx=920
    rrx=880
    carnums=0
    carlist=[]
    while(ref):
        # 读取某一帧
        # 格式转变，BGRtoRGB
        i+=1
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
       
        
        # 进行检测
        if i% 5==0:
             # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
            r_image,i,m= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist)
            draw = ImageDraw.Draw(r_image)
            draw.line((260,850,1500,850),fill='red',width=5)
            trfn=i
            carn=m
            frame = np.array(r_image)
            #frame = np.array(yolo.detect_image(frame))

            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            video_writer.write(frame)
        else:
            video_writer.write(frame)
        ref,frame=video_reader.read()

    video_reader.release()
    video_writer.release()
    yolo.close_session()
    keras.backend.clear_session()
    
   

