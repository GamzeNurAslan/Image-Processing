import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

im1 = Image.open("../images/yz.png")

im = np.array(im1)
io.imshow(im)
plt.axis('off'), plt.show()
