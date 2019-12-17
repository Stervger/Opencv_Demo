import numpy as np
import cv2


#画一个黑色背景
#大小为512*512,3表示BGR三种颜色,uint8是用0-255表示所有颜色
img=np.zeros((512,512,3), np.uint8)


#线条
#cv2.line(名称,(起点坐标),(终点坐标),(B,G,R),线条宽度)
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#矩形
# cv2.rectangle(名称,(左上顶点坐标),(右下顶点坐标),(B,G,R),线宽为3)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#圆
# cv2.circle(名称,(圆心坐标), 半径, (B,G,R), 线宽为-1,向内填充)
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#椭圆
# cv2.ellipse(名称,(中心点坐标),(长轴长度,短轴长度),椭圆整体旋转角度,隐藏的角度(以椭圆长轴右半轴顺时针开始),显示的角度(以椭圆长轴右半轴顺时针开始),255,-1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)

#多边形
#构建一个4行2列的数组,行数为就是顶点数目,数组类型必须为int32
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32).reshape((-1,1,2))
#第三个参数如果为False,则图形不闭合
# pts = pts.reshape((-1,1,2))
#名称,点集,是否闭合,颜色
cv2.polylines(img,[pts],True,(0,255,255))
#用cv2.polylines画多条直线
line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))

#添加文字
#自定义字体
font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'要加入的文字',(起始坐标,左下角开始), 字体, 字号,(255,255,255),2)
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,lineType=cv2.LINE_AA)

cv2.imshow('img',img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s') or k ==ord('S'):
    cv2.imwrite('Draw.jpg',img)






"""
    滑动块
"""

# # 回调函数，x表示滑块的位置，本例暂不使用
# def nothing(x):
#     pass
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('image')

# # 创建RGB三个滑动条
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
#
# while(True):
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) == 27:
#         break
#
#     # 获取滑块的值
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     # 设定img的颜色
#     img[:] = [b, g, r]