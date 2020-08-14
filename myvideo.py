#-------------------------------------#
#       调用摄像头检测
#-------------------------------------#
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import cv2


def detect(video_inputpath,video_outpath):
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
    carlistnums=0
    run_a_red_light=0
    totalcarn=0
    while(ref):
        # 读取某一帧
        # 格式转变，BGRtoRGB
        # i+=1
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        
        # 进行检测
        # if i% 5==0:
        r_image,i,m,n,carlistnums,run_a_red_light,totalcarn= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist)
        draw = ImageDraw.Draw(r_image)
        draw.line((260,850,1500,850),fill='red',width=5)
        trfn=i
        carn=m
        carnums=n
        frame = np.array(r_image)
        #frame = np.array(yolo.detect_image(frame))

        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        video_writer.write(frame)
        ref,frame=video_reader.read()
        
    video_reader.release()
    video_writer.release()
    yolo.close_session()
    keras.backend.clear_session()

def detect2(video_inputpath,video_outpath,light_Pos):
   
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
    l=light_Pos[0]
    lrx=l*2.4+30
    rrx=l*2.4-30
    carnums=0
    carlist=[]
    carlistnums=0
    run_a_red_light=0
    totalcarn=0
    while(ref):
        # 读取某一帧
        # 格式转变，BGRtoRGB
        i+=1
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        font = ImageFont.truetype('font/simhei.ttf',28)
        
        # 进行检测
        if (i-1)% 5==0:
             # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
            r_image,i,m,n,carlistnums,run_a_red_light,totalcarn= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist)
            draw = ImageDraw.Draw(r_image)
            draw.line((260,850,1500,850),fill='red',width=5)
            trfn=i
            carn=m
            carnums=n
            frame = np.array(r_image)
            #frame = np.array(yolo.detect_image(frame))

            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            video_writer.write(frame)
        else:
            frame = Image.fromarray(np.uint8(frame))

            draw = ImageDraw.Draw(frame)
            draw.rectangle(
                (1300,150,1900,200),
                fill="white")
            draw.text((1300,160,1900,180), "路口通过car的数量为:"+str(carlistnums), fill="black",font=font) 

            draw.rectangle(
                (1300,50,1900,140),
                fill="white")
            if totalcarn>=10:
                draw.text((1300,60,1900,100), "当前路口机动车数量为"+str(totalcarn)+"大于9"+"  拥堵",font=font) 
            else:
                draw.text((1300,60,1800,100), "当前路口机动车数量："+str(totalcarn), fill="black",font=font) 
            draw.text((1300,100,1800,140), "当前路口闯红灯数量："+str(run_a_red_light), fill="black",font=font)
            
            del draw

            frame = np.array(frame)
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            video_writer.write(frame)
        ref,frame=video_reader.read()

    video_reader.release()
    video_writer.release()
    yolo.close_session()
    keras.backend.clear_session()
    
   

