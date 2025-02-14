import os
import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np
from scipy import signal
import scipy.ndimage as ndimage
import numpy.fft as fp

image_path = 'C:/Users/aslan/PycharmProjects/openCV/images/me.png'

im = np.mean(imread(image_path), axis=2)

freq = fp.fft2(im)

freq_gaussian = ndimage.fourier_gaussian(freq, sigma=4)

im1 = fp.ifft2(freq_gaussian)

fig, (axes1, axes2) = plt.subplots(1, 2, figsize=(20,10))
plt.gray()

axes1.imshow(im)
axes1.axis('off')

axes2.imshow(im1.real)
axes2.axis('off')

plt.show()
