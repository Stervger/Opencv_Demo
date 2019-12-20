import cv2
import numpy as np

img = cv2.imread('D:\Opencv_Demo\Picture\pic\chessboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


"""
    Harris角点检测
"""
#转为float32的输入图像
gray = np.float32(gray)
#第一个参数为图像
#第二个参数blockSize为检测中要考虑的领域大小
#第三个参数ksize-Sobel为求导中使用的窗口大小
#第四个参数k-Harris为角点检测方程中的自由参数，取值参数为[0.04,0.06]
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)

img[dst>0.01*dst.max()] = [0,0,225]

cv2.imshow('dst',img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()