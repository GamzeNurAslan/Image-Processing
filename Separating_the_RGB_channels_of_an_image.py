import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("../images/yz.png")

ch_r, ch_g, ch_b = im1.split()

plt.figure(figsize=(18,6))

plt.subplot(1,3,1); plt.imshow(ch_r, cmap=plt.cm.Reds); plt.axis('off'); plt.title('Red Channel')
plt.subplot(1,3,2); plt.imshow(ch_g, cmap=plt.cm.Greens); plt.axis('off'); plt.title('Green Channel')
plt.subplot(1,3,3); plt.imshow(ch_b, cmap=plt.cm.Blues); plt.axis('off'); plt.title('Blue Channel')

plt.tight_layout()
plt.show()
