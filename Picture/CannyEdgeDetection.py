import cv2
import numpy as np



Origin = cv2.imread('D:\Opencv_Demo\Picture\pic\Hand.jpg',0)
img = cv2.resize(Origin,(560,650))
"""
    Canny边缘检测
"""
Canny = cv2.Canny(img,30,70)

"""
    先用Otsu自动阈值，再边缘检测
"""
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
Otsu_Canny= cv2.Canny(thresh,30,70)

cv2.namedWindow('Otsu_Canny',cv2.WINDOW_NORMAL)
cv2.imshow('Origin',img)
cv2.imshow('canny',Canny)
cv2.imshow('Otsu_Canny',Otsu_Canny)
cv2.waitKey(0)


"""
    用滑动条观测阈值
"""
# def track_back(x):
#     pass
#
# sudoku = cv2.imread('D:\Opencv_Demo\Picture\pic\sudoku.jpg',0)
# cv2.namedWindow('window')
#
# #创建滑动条
# cv2.createTrackbar('maxVal','window',100,255,track_back)
# cv2.createTrackbar('minVal','window',200,255,track_back)
#
# while(True):
#     max_val = cv2.getTrackbarPos('maxVal','window')
#     min_val = cv2.getTrackbarPos('minVal','window')
#
#     edges = cv2.Canny(sudoku,min_val,max_val)
#     cv2.imshow('window',edges)
#
#     #按下esc退出
#     if cv2.waitKey(0) == 27:
#         break










