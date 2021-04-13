import cv2
import numpy as np
import math
import copy as cp

drawing = False
mode = True
ix,iy = -1,-1
pre_img = np.zeros((512,512,3), np.uint8)
img = np.zeros((512,512,3), np.uint8)

def nothing(x):
    pass

def draw_circle(event, x, y, flags, param):
    global ix,iy,drawing,mode,pre_img,img
    
    # 每次获取当前Trackbar的位置
    r = cv2.getTrackbarPos('R', 'hello')
    g = cv2.getTrackbarPos('G', 'hello')
    b = cv2.getTrackbarPos('B', 'hello') 
    colors=(b,g,r)    
   
    print(colors) 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cp.deepcopy(pre_img)
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x,y), colors, -1)
            else:
                length = int(math.sqrt((ix-x)**2+(iy-y)**2)/2)
                center = (int(float(ix+x)/2), int(float(iy+y)/2))
                cv2.circle(img, center, length, colors, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix,iy), (x,y), colors,-1)
        else:
            length = int(math.sqrt((ix-x)**2+(iy-y)**2)/2)
            center = (int(float(ix+x)/2), int(float(iy+y)/2))
            cv2.circle(img, center, length, colors, -1)
        pre_img=img
   
   
# 创建面板       
cv2.namedWindow('hello')

# 在面板'hello'上，创建3个trackbar，分别命名为R,G,B,回调函数都是啥都不做
cv2.createTrackbar('R', 'hello', 0,255, nothing)
cv2.createTrackbar('G', 'hello', 0,255, nothing)
cv2.createTrackbar('B', 'hello', 0,255, nothing)

# 创建鼠标事件的回调函数
cv2.setMouseCallback('hello', draw_circle)

while(1):
    cv2.imshow('hello',img)
    k = cv2.waitKey(1) & 0xFF
    # 每次按'm'键都会切换状态，当m=True时，绘制矩形，m=False,绘制圆
    if k == ord('m'):
        mode = not mode
        
    # 如果按了'ESC'键，则关闭面板
    elif k == 27:
        break
    
cv2.destroyAllWindows()
