from skimage.util import img_as_float, random_noise
import cv2
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

im = img_as_float(io.imread("../images/yzx.jpg"))
plt.figure(figsize=(15,12))
sigmas = [0.1, 0.25, 0.5, 1]
for i in range(4):
    noisy = random_noise(im, var=sigmas[i]**2)
    plt.subplot(2,2,i+1)
    plt.imshow(noisy)
    plt.axis('off')
plt.title('Gaussian noise with sigma=' + str(sigmas[i]), size=20)
plt.tight_layout()
plt.show()
