import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    图像平滑
"""
img = cv2.imread('D:\Opencv_Demo\Picture\pic\p2.png')
#2D卷积
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)

#平均
# blur = cv2.blur(img,(5,5))

#高斯模糊
# blur = cv2.GaussianBlur(img,(5,5),0)

#中值模糊
median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('After')
plt.xticks([]),plt.yticks([])
plt.show()