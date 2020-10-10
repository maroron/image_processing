import cv2
import numpy as np
from matplotlib import pyplot as plt

img_green = cv2.imread('data/1.png', 0)
img_normal = cv2.imread('data/2.png', 0)
img_blue = cv2.imread('data/3.png', 0)

titles = ['green', 'normal', 'blue']
images = [img_green, img_normal, img_blue]
cnt = len(images)

for i in range(cnt * 3):
    # 1行目 画像の出力
    if i < cnt:
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
   
    # 2行目 ヒストグラムの表示
    elif i < cnt * 2:
        plt.subplot(3, 3, i+1)        
        plt.hist(images[i - cnt].flatten(), 256, [0, 256])
        plt.axis([0, 255, 0, 3000])

    # 3行目 ヒストグラムと画素値の累積分布関数の表示
    else:
        plt.subplot(3, 3, i+1)
        hist, bins = np.histogram(images[i - cnt * 2].flatten(), 256,[0,256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        plt.plot(cdf_normalized, color = 'b')
        plt.hist(images[i - cnt * 2].flatten(), 256, [0, 256])

plt.subplots_adjust(wspace=0.5)
plt.show()

