import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/yz.png")

methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'lanczos']

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 12), subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(hspace=0.05, wspace=0.05)

im1_np = np.array(im1)

for ax, interp_method in zip(axes.flat, methods):
    ax.imshow(im1_np, interpolation=interp_method)  
    ax.set_title(str(interp_method), size=20)

plt.tight_layout()
plt.show()
