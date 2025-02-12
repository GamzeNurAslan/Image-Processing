import cv2
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray

im = rgb2gray(io.imread("C:/Users/aslan/PycharmProjects/openCV/images/yzx.jpg"))  

plt.figure(figsize=(20,8))

plt.subplot(131)
plt.imshow(im, cmap='gray')
plt.title('Original Image', size=20)

plt.subplot(132)
plt.contour(np.flipud(im), colors='k', levels=np.logspace(-15, 15, 100))
plt.title('Image Contour Lines', size=20)

plt.subplot(133)
plt.contourf(np.flipud(im), cmap='inferno')
plt.title('Image Filled Contour', size=20)

plt.show()
