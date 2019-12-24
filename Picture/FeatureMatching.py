import cv2
import numpy as np
from matplotlib import pyplot as plt

#读取图片，格式为灰度图
target = cv2.imread('D:\Opencv_Demo\Picture\pic\Target.jpg',0)
template = cv2.imread('D:\Opencv_Demo\Picture\pic\Template.jpg',0)


"""
    对 ORB 描述符进行蛮力匹配
    
"""
# #初始化一个orb对象（建立orb特征检测器）
# orb = cv2.ORB_create()
#
# #用SIFT找到关键点和描述符
# template_kp,template_des = orb.detectAndCompute(template,None)  #计算模板中的特征点和描述符
# target_kp,target_des = orb.detectAndCompute(target,None)        #计算目标中的特征点和描述符
#
# #创建BFMatcher对象，建立匹配关系（蛮力匹配）
# bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
#
# #匹配描述符
# matches = bf.match(template_des,target_des)
# #按距离来排序
# matches = sorted(matches, key = lambda x:x.distance)
# #画出匹配
# img = cv2.drawMatches(target,target_kp,template,template_kp,matches[:40],None, flags=2)

"""
    对 SIFT 描述符进行蛮力匹配和比值测试

"""
# #创建sift检测器
# sift = cv2.xfeatures2d.SIFT_create()
#
# template_kp,template_des = sift.detectAndCompute(template,None)  #计算模板中的特征点和描述符
# target_kp,target_des = sift.detectAndCompute(target,None)        #计算目标中的特征点和描述符
#
# #设置flannde参数
# FLANN_INDEX_KDTREE = 0
# indexParams = dict(algoithm = FLANN_INDEX_KDTREE,trees=5)
# searchParams = dict(checks = 50)
# flann = cv2.FlannBasedMatcher(indexParams,searchParams)
# matches = flann.knnMatch(template_des,target_des,k=2)
#
# #设置初始匹配值
# matchesMask = [[0,0] for i in range (len(matches))]
# for i , (m,n) in enumerate(matches):
#     if m.distance < 0.5*n.distance:
#         matchesMask[i]=[1,0]
# drawParams = dict(matchColor=(0,0,255),singlePointColor = (255,0,0),matchesMask=matchesMask,flage=0)
# resultimage=cv.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams) #画出匹配的结果
# plt.imshow(resultimage,),plt.show()

sift = cv2.SIFT()#创建sift检测器
kp1, des1 = sift.detectAndCompute(template,None)
kp2, des2 = sift.detectAndCompute(target,None)
#设置Flannde参数
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams= dict(checks=50)
flann=cv2.FlannBasedMatcher(indexParams,searchParams)
matches=flann.knnMatch(des1,des2,k=2)
#设置好初始匹配值
matchesMask=[[0,0] for i in range (len(matches))]
for i, (m,n) in enumerate(matches):
	if m.distance< 0.5*n.distance: #舍弃小于0.5的匹配结果
		matchesMask[i]=[1,0]
drawParams=dict(matchColor=(0,0,255),singlePointColor=(255,0,0),matchesMask=matchesMask,flags=0) #给特征点和匹配的线定义颜色
resultimage=cv2.drawMatchesKnn(template,kp1,target,kp2,matches,None,**drawParams) #画出匹配的结果
plt.imshow(resultimage,),plt.show()










# cv2.imshow('img',img)
#
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()



































































































































