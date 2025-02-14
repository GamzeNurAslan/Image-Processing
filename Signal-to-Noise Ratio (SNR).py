import os
from PIL import Image
import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np
from scipy import signal
import scipy.ndimage as ndimage
import numpy.fft as fp
from skimage.restoration import denoise_tv_chambolle
from scipy import fftpack

image_path = 'C:/Users/aslan/PycharmProjects/openCV/images/me.png'

im = np.array(Image.open(image_path).convert('L'))

freq = fp.fft2(im)

(w, h) = freq.shape
half_w, half_h = int(w / 2), int(h / 2)

snrs_hp = []
lbs = list(range(1, 25))

plt.figure(figsize=(12, 20))

for l in lbs:
    freq1 = np.copy(freq)
    freq2 = fftpack.fftshift(freq1)

    freq2[half_w - l:half_w + l + 1, half_h - l:half_h + l + 1] = 0

    im1 = np.clip(fp.ifft2(fftpack.ifftshift(freq2)).real, 0, 255)

    snr = np.std(im1) / np.mean(np.abs(im1 - np.mean(im1)))
    snrs_hp.append(snr)

    plt.subplot(6, 4, l), plt.imshow(im1, cmap='gray'), plt.axis('off')
    plt.title(f'F = {l + 1}', size=20)

plt.subplots_adjust(wspace=0.1, hspace=0)
plt.show()
