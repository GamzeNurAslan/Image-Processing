import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("../images/yz.png")
im2 = Image.open("../images/me.png").convert('RGB').resize((im1.width, im1.height))

im1 = im1.convert('RGBA')
im2 = im2.convert('RGBA')

im = Image.blend(im1, im2, alpha=0.5)

plt.figure(figsize=(10, 10))
plt.imshow(im)
plt.axis('off')
plt.title("Blended Image")
plt.show()
