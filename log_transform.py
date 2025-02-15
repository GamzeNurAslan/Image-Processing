import matplotlib.pylab as pylab
import numpy as np
from skimage.util import img_as_ubyte
from PIL import Image

def plot_image(image, title=''):
    pylab.title(title, size=20)
    pylab.imshow(image)
    pylab.axis('off')  

def plot_hist(r, g, b, title=''):
    r, g, b = img_as_ubyte(r), img_as_ubyte(g), img_as_ubyte(b)
    pylab.hist(np.array(r).ravel(), bins=256, range=(0, 256), color='r', alpha=0.5)
    pylab.hist(np.array(g).ravel(), bins=256, range=(0, 256), color='g', alpha=0.5)
    pylab.hist(np.array(b).ravel(), bins=256, range=(0, 256), color='b', alpha=0.5)
    pylab.xlabel('pixel value', size=20)
    pylab.ylabel('frequency', size=20)
    pylab.title(title, size=20)

im = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/me.png")

print(f"Görüntü formatı: {im.mode}")

if im.mode == 'RGBA':
    im = im.convert('RGB')

im_r, im_g, im_b = im.split()

pylab.style.use('ggplot')
pylab.figure(figsize=(15, 5))

pylab.subplot(121), plot_image(im, 'original image')

pylab.subplot(122), plot_hist(im_r, im_g, im_b, 'histogram for RGB channels')

pylab.show()
