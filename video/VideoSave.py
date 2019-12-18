import numpy as np
import cv2

#加载视频
cap = cv2.VideoCapture(r'D:\Opencv_Demo\video\video.mp4')
print(cap.isOpened())
#自定义编码方式并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')#自定义编码方式
outfile = cv2.VideoWriter('output.mp4',fourcc,20.,(1920,1080))
while(cap.isOpened()):
    ret,frame = cap.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==True:
        frame = cv2.flip(frame, 0)
        outfile.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()