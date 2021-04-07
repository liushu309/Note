import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img1 = cv2.imread('img/m.jpg', 0)  # queryimage # 左侧图片
img2 = cv2.imread('img/n.jpg', 0)  # trainimage # 右侧图片
 
sift = cv2.xfeatures2d.SIFT_create()
 
# 用SIFT查找关键点和描述子
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
 
# FLANN参数
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
 
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1, des2, k=2)
 
good = []
pts1 = []
pts2 = []
 
# 按照Lowe的论文进行比率测试
for i, (m, n) in enumerate(matches):
     if len(good) > 10:
        break
    if m.distance < 0.8*n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)


pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_LMEDS)
 
# 我们只使用inlier点
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]


def drawlines(img1, img2, lines, pts1, pts2):
    ''' img1 - 我们要绘制到的图像
        lines - 相应的极线 '''
    r, c = img1.shape
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2]/r[1]])
        x1, y1 = map(int, [c, -(r[2]+r[0]*c)/r[1]])
        img1 = cv2.line(img1, (x0, y0), (x1, y1), color, 1)
        img1 = cv2.circle(img1,tuple(pt1), 5, color, -1)
        img2 = cv2.circle(img2,tuple(pt2), 5, color, -1)
    return img1, img2




# 找到右边图像（第二张图像）中的点对应的极线，在左边图像上画出来
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
lines1 = lines1.reshape(-1, 3)
img5, img6 = drawlines(img1, img2, lines1, pts1, pts2)
 
# 找到左边图像（第一张图像）中的点对应的极线
# 在右边图像上画出来
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
lines2 = lines2.reshape(-1, 3)
img3, img4 = drawlines(img2, img1, lines2, pts2, pts1)
 
plt.subplot(121), plt.imshow(img5)
plt.subplot(122), plt.imshow(img3)
plt.savefig('sift_left_right.png')
plt.show()

