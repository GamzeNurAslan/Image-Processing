import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("../images/me.png")

im_np = np.array(im)

plt.imshow(im_np)
plt.axis('off')
plt.show()
