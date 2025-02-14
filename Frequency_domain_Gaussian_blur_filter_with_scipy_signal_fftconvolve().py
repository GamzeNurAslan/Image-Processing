from skimage.io import imread
import matplotlib.pylab as pylab
import numpy as np
from scipy import signal
from scipy.stats import norm

im = np.mean(imread('C:/Users/aslan/PycharmProjects/openCV/images/me.png'), axis=2)
print(im.shape)

gauss_kernel = np.outer(norm.pdf(np.linspace(-3, 3, 11), 0, 3), norm.pdf(np.linspace(-3, 3, 11), 0, 3))

im_blurred = signal.fftconvolve(im, gauss_kernel, mode='same')

fig, (ax_original, ax_kernel, ax_blurred) = pylab.subplots(1, 3, figsize=(20,8))

ax_original.imshow(im, cmap='gray')
ax_original.set_title('Original', size=20)
ax_original.set_axis_off()

ax_kernel.imshow(gauss_kernel)
ax_kernel.set_title('Gaussian kernel', size=15)
ax_kernel.set_axis_off()

ax_blurred.imshow(im_blurred, cmap='gray')
ax_blurred.set_title('Blurred', size=20)
ax_blurred.set_axis_off()

fig.tight_layout()
pylab.show()

# Programın sonlanmasını engellemek için kullanıcıdan bir tuş girişi bekleyelim.
input("Press Enter to exit...")
