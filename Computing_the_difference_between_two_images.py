from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/yz.png")
im2 = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/me.png")

im1 = im1.resize(im2.size)

im1 = im1.convert("RGB")
im2 = im2.convert("RGB")

im = ImageChops.difference(im1, im2)
plt.figure(figsize=(20,25))

plt.subplot(311)
plt.imshow(im1)
plt.axis('off')
plt.subplot(312)
plt.imshow(im2)
plt.axis('off')
plt.subplot(313)
plt.imshow(im), plt.axis('off')
plt.show()
