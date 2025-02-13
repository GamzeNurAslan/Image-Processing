import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("../images/me.png")

im_np = np.array(im)

plt.imshow(im_np)
plt.axis('off')
plt.show()

#-----------------------------------------#

"""Nearest"""
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/me.png")

im1 = im.resize((im.width*5, im.height*5), Image.NEAREST) 
plt.figure(figsize=(10,10)), plt.imshow(im1), plt.show()

#----------------------------------------#

"""Bir resmi 10 kat büyütüp hem PIL.Image.show() ile gösterir,
hem de büyütülmüş resmi matplotlib kullanarak ekranda görselleştirir"""
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("C:/Users/aslan/PycharmProjects/openCV/images/me.png")

resized_im = im.resize((im.width*10, im.height*10), Image.BICUBIC)

resized_im.show()

im_np = np.array(resized_im)

plt.figure(figsize=(10,10))
plt.imshow(im_np)
plt.axis('off')  # Eksenleri kaldırır
plt.show()

#-----------------------------------------#


