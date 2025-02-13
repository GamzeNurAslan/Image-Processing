from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
import numpy.fft as fp
import cv2

im = io.imread('C:/Users/aslan/PycharmProjects/openCV/images/me.png')
im2 = io.imread('C:/Users/aslan/PycharmProjects/openCV/images/yz.png')

if im.shape[2] == 4:
    im = im[:, :, :3]  #sadece RGB

if im2.shape[2] == 4:
    im2 = im2[:, :, :3]  #sadece RGB

im_gray = rgb2gray(im)
im2_gray = rgb2gray(im2)

im2_gray_resized = cv2.resize(im2_gray, (im_gray.shape[1], im_gray.shape[0]))

freq1 = fp.fft2(im_gray)
freq2 = fp.fft2(im2_gray_resized)

im1_ = fp.ifft2(np.vectorize(complex)(freq1.real, freq2.imag)).real
im2_ = fp.ifft2(np.vectorize(complex)(freq2.real, freq1.imag)).real

plt.figure(figsize=(20, 15))
plt.subplot(211), plt.imshow(np.clip(im1_, 0, 255), cmap='gray')
plt.title('Reconstructed Image (Re(F1) + Im(F2))', size=20)
plt.subplot(212), plt.imshow(np.clip(im2_, 0, 255), cmap='gray')
plt.title('Reconstructed Image (Re(F2) + Im(F1))', size=20)
plt.show()
