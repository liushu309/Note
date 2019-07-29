#coding: utf-8
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
leftgray = cv2.imread('sub/camera_7.jpg')
rightgray = cv2.imread('sub/camera_8.jpg')

h,w=leftgray.shape[:2]
scale_size = 4
leftgray = cv2.resize(leftgray, (int(w / scale_size), int(h / scale_size)))
rightgray = cv2.resize(rightgray, (int(w / scale_size), int(h / scale_size)))
h,w=leftgray.shape[:2]

surf=cv2.xfeatures2d.SURF_create() #将Hessian Threshold设置为400,阈值越大能检测的特征就越少
kp1,des1=surf.detectAndCompute(leftgray,None)  #查找关键点和描述符
kp2,des2=surf.detectAndCompute(rightgray,None)


flann=cv2.FlannBasedMatcher()  #建立匹配器
matches=flann.match(des1,des2)  #得出匹配的关键点
src_pts = np.array([ kp1[m.queryIdx].pt for m in matches])    #查询图像的特征描述子索引
dst_pts = np.array([ kp2[m.trainIdx].pt for m in matches])    #训练(模板)图像的特征描述子索引

H, mask = cv2.findHomography(src_pts,dst_pts, cv2.RANSAC, 5.0, np.zeros(src_pts.shape), 500)         #生成变换矩阵

dst_corners=cv2.warpPerspective(leftgray,H,(w*2,h*2))#透视变换，新图像可容纳完整的两幅图

# rightgray.copyTo(dst_corners(Rect(0, 0, w, h)))
dst_corners[:h, 0:w:, :] = rightgray

fig, ax = plt.subplots(1, 1, figsize=(16, 4))
ax.imshow(dst_corners[:, :, : :-1])
# ax[0].imshow(dst_corners[:, :, : :-1])
# ax[1].imshow(rightgray[:, :, : :-1])
# ax[2].imshow(leftgray[:, :, : :-1])

cv2.imwrite('ret/tiledImg1.jpg',dst_corners)   #显示，第一幅图已在标准位置
