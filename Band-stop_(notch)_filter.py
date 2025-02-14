import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from scipy.fft import fft2, ifft2, fftshift
from scipy import fftpack

plt.figure(figsize=(15,10))
im =  np.mean(imread("C:/Users/aslan/PycharmProjects/openCV/images/me.png"), axis=2) / 255
print(im.shape)
plt.subplot(2,2,1), plt.imshow(im, cmap='gray'), plt.axis('off')
plt.title('Original Image')
F1 = fftpack.fft2((im).astype(float))
F2 = fftpack.fftshift( F1 )
plt.subplot(2,2,2), plt.imshow( (20*np.log10( 0.1 + F2)).astype(int), cmap=plt.cm.gray)
plt.xticks(np.arange(0, im.shape[1], 25))
plt.yticks(np.arange(0, im.shape[0], 25))
plt.title('Original Image Spectrum')
for n in range(im.shape[1]):
    im[:, n] += np.cos(0.1*np.pi*n)
plt.subplot(2,2,3), plt.imshow(im, cmap='gray'), plt.axis('off')
plt.title('Image after adding Sinusoidal Noise')
F1 = fftpack.fft2((im).astype(float))
F2 = fftpack.fftshift( F1 )
plt.subplot(2,2,4), plt.imshow( (20*np.log10( 0.1 + F2)).astype(int), cmap=plt.cm.gray)
plt.xticks(np.arange(0, im.shape[1], 25))
plt.yticks(np.arange(0, im.shape[0], 25))
plt.title('Noisy Image Spectrum')
plt.tight_layout()
plt.show()
