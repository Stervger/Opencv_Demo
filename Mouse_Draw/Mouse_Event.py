import numpy as np
import cv2


"""
    使用鼠标回调函数,输出鼠标当前点击坐标
"""
# #鼠标的回调函数用看来知道鼠标的当前位置
# #回调函数参数格式固定
# def mouse_event(event,x,y,flags,param):
#     #通过event判断具体是什么事件
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#
# #创建窗口(大小为512*512,3种颜色)
# img = np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# #定义鼠标回调函数
# cv2.setMouseCallback('image',mouse_event)
#
# while(True):
#     cv2.imshow('image',img)
#     if cv2.waitKey() == 27:
#         break

drawing = False #一开始设置为关闭画图
mode = True #画图模式,True为矩形,False为圆形
start = (-1,-1) #线宽为-1表示填充

def mouse_event(event,x,y,flags,param):
    global start,drawing,mode #将变量定义为全局变量

    #左键按下开始画图
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x,y)
    #鼠标移动,画图
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img,start,(x,y),(0,255,0),1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    #左键释放结束画图
    elif event ==cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img,start,(x,y),(0,255,0),1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_event)

while(True):
    cv2.imshow('image',img)
    #按下m切换画图模式
    if cv2.waitKey(1) == ord('m'):
        mode = not mode
    elif cv2.waitKey(1) == 27:
        break










