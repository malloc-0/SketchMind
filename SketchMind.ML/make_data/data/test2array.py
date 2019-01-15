# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pylab as plt
# 加载图像
# im = plt.imread("BTD.jpg") # 加载当前文件夹中名为BTD.jpg的图片


img = cv2.imread('data/test1.png')
print (img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print (gray[1])

cv2.imwrite("gray.jpg", img)

g_new0 = cv2.imread('gray.jpg')
g_new1 = plt.imread("gray.jpg") # 加载当前文件夹中名为BTD.jpg的图片
print (g_new1.shape)
