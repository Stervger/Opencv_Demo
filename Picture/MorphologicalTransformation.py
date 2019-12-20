import cv2
import numpy as np

Origin = cv2.imread('D:\Opencv_Demo\Picture\pic\j.png',0)
open = cv2.imread('D:\Opencv_Demo\Picture\pic\j_with_whitedot_outside.png',0)
close = cv2.imread('D:\Opencv_Demo\Picture\pic\j_with_bclackdot_inside.png',0)
img = cv2.resize(Origin,(180,280))
opening_p = cv2.resize(open,(180,280))
closing_p = cv2.resize(close,(180,280))

"""
    腐蚀
"""
#指定一个5x5的卷积核
kernel = np.ones((5,5),np.uint8)
#第一个参数为要进行腐蚀操作的图
#第二个参数为腐蚀的内核
#第三个参数为腐蚀的次数，默认为1
erosion = cv2.erode(img,kernel,iterations=1)

"""
    膨胀
"""
dilation = cv2.dilate(img,kernel)

"""
    开运算
"""
opening = cv2.morphologyEx(
    opening_p,cv2.MORPH_OPEN,kernel
)

"""
    闭运算
"""
closing = cv2.morphologyEx(
    closing_p,cv2.MORPH_CLOSE,kernel
)



# cv2.imshow('Origin',img)

# cv2.imshow('erode',erosion)
# cv2.imshow('dilation',dilation)

cv2.imshow('open',open)
cv2.imshow('close',close)

cv2.imshow('opening',opening)
cv2.imshow('closing',closing)


cv2.waitKey(0)