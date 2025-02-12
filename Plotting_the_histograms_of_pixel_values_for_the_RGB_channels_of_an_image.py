import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/yz.png")

pl = im1.histogram()
plt.bar(range(256), pl[:256], color='r', alpha=0.5)
plt.bar(range(256), pl[256:2*256], color='g', alpha=0.4)
plt.bar(range(256), pl[2*256:], color='b', alpha=0.3)
plt.show()
