import cv2
import numpy as np

"""
    多边形逼近
"""
# img = cv2.imread('D:\Opencv_Demo\Picture\pic\MutiContour.jpg',0)
#
# #Otsu自动阈值
# _,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
# #找到轮廓
# contours,hierarchy = cv2.findContours(thresh,3,2)
# cnt = contours[0]
# print(len(contours))
#
# #进行多边形逼近
# approx = cv2.approxPolyDP(cnt,1,True)
#
# #画出多边形
# image = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# cv2.polylines(image,[approx],True,(0,255,0),2)
#
# cv2.imshow('image',image)
# cv2.waitKey(0)


"""
    凸包
"""

Origin = cv2.imread('D:\Opencv_Demo\Picture\pic\MutiContour.jpg',0)
img = cv2.resize(Origin,(560,650))
#Otsu自动阈值
_,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#找到轮廓
contours,hierarchy = cv2.findContours(thresh,3,2)
cnt = contours[0]
print(len(contours))

#找到凸包，得到凸包的角点
hull = cv2.convexHull(cnt)

#绘制凸包
image = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.polylines(image,[hull],True,(0,255,0),2)

cv2.imshow('image',image)
#判断是否是凸型图片
print(cv2.isContourConvex(hull))

cv2.waitKey(0)










