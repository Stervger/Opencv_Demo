import cv2
import numpy as np

cap = cv2.VideoCapture(r'D:\Opencv_Demo\video\video.mp4')

"""
物体颜色跟踪
"""
while(True):
    #提取每一帧
    ret,frame = cap.read()
    #将BGR转换为HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #自定义蓝色的范围
    lower_blue = np.array([100, 110, 110])
    upper_blue = np.array([130, 255, 255])

    #介于lower/upper之间为白色，其余黑色
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    #只保留原图中蓝色的部分
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) == ord('q'):
        break