import cv2
import numpy as np
from matplotlib import pyplot as plt

img_green = cv2.imread('data/1.png')
img_normal = cv2.imread('data/2.png')
img_blue = cv2.imread('data/3.png')
gb, gg, gr = img_green[:, :, 0], img_green[:, :, 1], img_green[:, :, 2]
nb, ng, nr = img_normal[:, :, 0], img_normal[:, :, 1], img_normal[:, :, 2]
bb, bg, br = img_blue[:, :, 0], img_blue[:, :, 1], img_blue[:, :, 2]

titles = ['green', 'normal', 'blue']
images = [img_green, img_normal, img_blue]
colors = [[gb, gg, gr], [nb, ng, nr], [bb, bg, br]]
cnt = len(images)
plt.figure(figsize=(10,8))

for i in range(cnt * 2):
    if i < cnt:
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i][:, :, ::-1], vmin=0, vmax=255, interpolation="none")
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    elif i < cnt * 2:
        plt.subplot(2, 3, i+1)        
        # plt.hist(images[i - cnt].flatten(), 256, [0, 256])
        plt.axis([0, 255, 0, 3000])

        hist_b = cv2.calcHist([colors[i-cnt][0]], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([colors[i-cnt][1]], [0], None, [256], [0, 256])
        hist_r = cv2.calcHist([colors[i-cnt][2]], [0], None, [256], [0, 256])

        plt.plot(hist_r, "-r", label="RED")
        plt.plot(hist_g, "-g", label="GREEN")
        plt.plot(hist_b, "-b", label="BLUE")
        plt.grid()

plt.subplots_adjust(wspace=0.25)
plt.show()

