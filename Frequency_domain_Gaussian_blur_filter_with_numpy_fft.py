from PIL import Image
from skimage.io import imread, imshow, show
import scipy.fftpack as fp
from scipy import ndimage, signal
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage.filters import gaussian
import matplotlib.pylab as pylab
import numpy as np
import numpy.fft
import timeit

pylab.figure(figsize=(20, 15))
pylab.gray()
im = np.mean(imread('../images/me.png'), axis=2)

gauss_kernel = gaussian(im, sigma=5)

freq = fp.fft2(im)
assert(freq.shape == gauss_kernel.shape)
freq_kernel = fp.fft2(fp.ifftshift(gauss_kernel))
convolved = freq * freq_kernel
im1 = fp.ifft2(convolved).real

pylab.subplot(2, 3, 1), pylab.imshow(im), pylab.title('Original Image', size=20), pylab.axis('off')
pylab.subplot(2, 3, 2), pylab.imshow(gauss_kernel), pylab.title('Gaussian Kernel', size=20)
pylab.subplot(2, 3, 3), pylab.imshow(im1)
pylab.title('Output Image', size=20), pylab.axis('off')
pylab.subplot(2, 3, 4), pylab.imshow((20 * np.log10(0.1 + fp.fftshift(freq))).astype(int))
pylab.title('Original Image Spectrum', size=20), pylab.axis('off')
pylab.subplot(2, 3, 5), pylab.imshow((20 * np.log10(0.1 + fp.fftshift(freq_kernel))).astype(int))
pylab.title('Gaussian Kernel Spectrum', size=20), pylab.subplot(2, 3, 6)
pylab.imshow((20 * np.log10(0.1 + fp.fftshift(convolved))).astype(int))
pylab.title('Output Image Spectrum', size=20), pylab.axis('off')
pylab.subplots_adjust(wspace=0.2, hspace=0)
pylab.show()
