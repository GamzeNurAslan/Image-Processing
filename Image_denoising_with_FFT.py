import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from scipy.fft import fft2, ifft2, fftshift

im = imread('../images/me.png').astype(float)

if im.ndim == 3:
    im = np.mean(im, axis=2)

im /= 255.0

noise = np.random.normal(0, 0.1, im.shape)
noisy_im = im + noise

fft_im = fft2(noisy_im)


def create_gaussian_filter(shape, cutoff_radius):
    rows, cols = shape

    center = (rows // 2, cols // 2)

    y, x = np.fft.fftfreq(rows), np.fft.fftfreq(cols)
    x, y = np.meshgrid(x, y)

    dist = np.sqrt((x - center[1]) ** 2 + (y - center[0]) ** 2)

    filter_mask = np.exp(-dist ** 2 / (2 * cutoff_radius ** 2))

    return filter_mask


cutoff_radius = 0.05

gaussian_filter = create_gaussian_filter(im.shape, cutoff_radius)
filtered_fft_im = fft_im * gaussian_filter

denoised_im = np.abs(ifft2(filtered_fft_im))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

#original image
axes[0].imshow(im, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')

#noisy image
axes[1].imshow(noisy_im, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Noisy Image')

#denoised image
axes[2].imshow(denoised_im, cmap='gray')
axes[2].axis('off')
axes[2].set_title('Denoised Image')

plt.tight_layout()
plt.show()
