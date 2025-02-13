import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

import numpy.fft as fp

im = io.imread('C:/Users/aslan/PycharmProjects/openCV/images/me.png')

if im.shape[2] == 4:
    im = im[:, :, :3] 

im1 = rgb2gray(im)

freq1 = fp.fft2(im1)

im1_ = fp.ifft2(freq1).real

plt.figure(figsize=(12, 10))

# 1. Orijinal Görüntü
plt.subplot(2, 2, 1)
plt.imshow(im1, cmap='gray')
plt.title('Original Image', size=20)

# 2. FFT Büyüklüğü 
plt.subplot(2, 2, 2)
plt.imshow(20 * np.log10(0.01 + np.abs(fp.fftshift(freq1))), cmap='gray')
plt.title('FFT Spectrum Magnitude', size=20)

# 3. FFT Fazı
plt.subplot(2, 2, 3)
plt.imshow(np.angle(fp.fftshift(freq1)), cmap='gray')
plt.title('FFT Phase', size=20)

# 4. Yeniden Yapılandırılmış Görüntü 
plt.subplot(2, 2, 4)
plt.imshow(np.clip(im1_, 0, 1), cmap='gray') 
plt.title('Reconstructed Image', size=20)

plt.show()

