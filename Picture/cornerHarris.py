import cv2
import numpy as np

img = cv2.imread('D:\Opencv_Demo\Picture\pic\Building.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


"""
    Harris角点检测
"""
# #转为float32的输入图像
# gray = np.float32(gray)
# #第一个参数为图像
# #第二个参数blockSize为检测中要考虑的领域大小
# #第三个参数ksize-Sobel为求导中使用的窗口大小
# #第四个参数k-Harris为角点检测方程中的自由参数，取值参数为[0.04,0.06]
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# dst = cv2.dilate(dst,None)
#
# img[dst>0.01*dst.max()] = [0,0,225]
#
# cv2.imshow('dst',img)


"""
    亚像素级精确角点检测
    
"""
# #先找到Harris角点
# dst = cv2.cornerHarris(gray,2,3,0.04)
# dst = cv2.dilate(dst,None)
# ret,dst = cv2.threshold(dst,0.01*dst.max(),255,0)
# dst = np.uint8(dst)
#
# #找到重心
# ret,label,state,centroids = cv2.connectedComponentsWithStats(dst)
#
# #定义停止迭代和细化角点的条件
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,100,0.001)
# corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,6),(-1,-1),criteria)
#
# res = np.hstack((centroids,corners))
# res = np.int0(res)
# #Harris 角点用红色像素标出
# img[res[:,1],res[:,0]] = [0,0,255]
# #绿色像素是修正后的像素
# img[res[:,3],res[:,2]] = [0,255,0]
#
# cv2.imshow('img',img)

"""
    Shi-Tomasi 角点检测 & 适合于跟踪的图像特征
    
"""
#第一个参数为图像
#第二个参数为要返回的角点数
#第三个参数为图像角点的最小可接受参数，质量测量值乘以这个参数就是最小特征值，小于这个数的会被抛弃
#第四个参数为返回的角点之间最小的欧式距离
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('img',img)

"""
    SURF（版本问题不能跑）

"""
# #设置Hessian阈值
# surf = cv2.xfeatures2d.SURF_create(400)
#
# #查找关键字和描述符
# kp, des = surf.detectAndCompute(img,None)
#
# len(kp)

"""
    
    FAST算法
"""
# #初始化一个fast对象
# fast = cv2.FastFeatureDetector_create()
#
# #找到并画出关键点
# kp = fast.detect(img,None)
# img2 = cv2.drawKeypoints(img, kp,img ,color=(255,0,0))
#
# #打印所有默认参数
# # print ("Threshold: ", fast.getInt('Threshold'))                      #阈值
# # print ("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))     #非最大值抑制
# # print ("neighborhood: ", fast.getInt('type'))                        #邻域大小
# # print ("Total Keypoints with nonmaxSuppression: ", len(kp))          #非最大值抑制下的关键点数量
#
# cv2.imshow('img2',img2)
#
# # #取消非最大值抑制(版本问题无法实现)
# # fast.setBool('nonmaxSuppression',0)
# # kp = fast.detect(img,None)
# # img3 = cv2.drawKeypoints(img,kp,img,color=(0,255,0))

"""
    ORB算法
    
"""
# #初始化ORB对象
# orb = cv2.ORB()
#
# #用orb找到关键点
# kp = orb.detect(img,None)
#
# #用orb进行计算
# kp,des = orb.compute(img ,kp)
#
# #只画出关键点位置，不画大小和方向
# img2 = cv2.drawKeypoints(img,kp,color=(0,255,0),flags=0)

# cv2.imshow('img2',img2)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()



