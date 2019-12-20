import numpy as np
import cv2

img = cv2.imread('D:\Opencv_Demo\Picture\pic\handwriting.jpg')
#转为灰度图
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#OTSU阈值
ret,thresh = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#寻找二值化中的轮廓
# 参数2：轮廓的查找方式，一般使用cv2.RETR_TREE，表示提取所有的轮廓并建立轮廓间的层级。
# 参数3：轮廓的近似方法。
#这两个参数也可以直接用3,2表示
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#轮廓数量
print(len(contours))
#绘制轮廓
cnt = contours[0]
cv2.drawContours(img,[cnt],-1,(0,0,255),2)

"""
    轮廓属性
"""
#轮廓面积()只有封闭图形才有效
area = cv2.contourArea(cnt)
print(area)

#轮廓周长()第二个参数用来指定对象的形状是闭合（True）还是打开的（一条曲线）
perimeter = cv2.arcLength(cnt,True)
print(perimeter)

cv2.imshow('contours',img)
cv2.waitKey(0)