from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import gaussian
import scipy.fftpack as fp
import matplotlib.pylab as pylab
import numpy as np
from scipy import signal

im = imread('C:/Users/aslan/PycharmProjects/openCV/images/me.png')

# Eğer resim RGBA ise, alfa kanalını çıkar ve sadece RGB'yi al
if im.shape[2] == 4:
    im = im[:, :, :3]  # sadece RGB

im_gray = rgb2gray(im)

gauss_kernel = gaussian(im_gray, sigma=1)

freq = fp.fft2(im_gray)
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))

log_freq_kernel = 20 * np.log10(0.01 + np.abs(fp.fftshift(freq_kernel)))

pylab.imshow(log_freq_kernel, cmap='coolwarm')
pylab.colorbar()
pylab.show()


