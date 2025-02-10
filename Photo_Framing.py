import cv2
import matplotlib.pyplot as plt

img = cv2.imread('yz.png')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#BORDER_REPLICATE
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
replicate_rgb = cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB)
#BORDER_REFLECT
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect_rgb = cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB)
#BORDER_REFLECT_101
reflect_101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
reflect_101_rgb = cv2.cvtColor(reflect_101, cv2.COLOR_BGR2RGB)
#BORDER_WRAP
wrap =cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
wrap_rgb = cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB)
#BORDER_CONSTANT
greenColor = (0, 255, 0)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, greenColor)
constant_rgb = cv2.cvtColor(constant, cv2.COLOR_BGR2RGB)

#cv2.imshow('main', img)
#cv2.imshow('replicate', replicate)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.subplot(2, 3, 1), plt.imshow(img), plt.title('ORIGINAL')
plt.subplot(2, 3, 2), plt.imshow(replicate), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect_101), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant), plt.title('CONSTANT')
plt.show()
