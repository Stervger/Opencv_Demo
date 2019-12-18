import numpy as np
import cv2
from matplotlib import pyplot as plt


"""
    opencv读取图片加载后显示图片，
    ESC直接退出
    S保存后退出
"""
#读取图片
img = cv2.imread('D:\Opencv_Demo\Picture\p1.jpg',1)
#获取某像素点的值
px = img[10,10]
print(px)
#只获取蓝色通道的值
px_blue = img[100,100,0]
print(px_blue)
#获取图像总像素
print(img.size)
# #指定图片ROI区域，（感兴趣区域）
# face = img[100:200,115:188]
#初始化窗口，使用WINDOW_NORMAL可以调整窗口大小
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#加载展示图片
cv2.imshow('image',img)
#waitkey为键盘绑定函数，时间单位为毫秒
k = cv2.waitKey(0)
if k == 27 : #ESC的ASK码值，按下后退出
    cv2.destroyAllWindows()
elif k == ord('s'): #按s保存后退出
    # 保存图片
    cv2.imwrite('01backup.jpg', img)
    #删除所有创建的窗口，删除特定窗口使用cv2.destroyWindow()，括号内填窗口名
    cv2.destroyAllWindows()

"""
    使用Matplotlib
"""
# img = cv2.imread('p1.jpg',1)
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()
























