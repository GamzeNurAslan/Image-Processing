import cv2
from skimage import io
from matplotlib import pyplot as plt
from skimage.transform import swirl

im = io.imread("C:/Users/aslan/PycharmProjects/openCV/images/yzx.jpg")
swirled = swirl(im, rotation=0, strength=15, radius=200)
plt.imshow(swirled)
plt.axis('off')
plt.show()
