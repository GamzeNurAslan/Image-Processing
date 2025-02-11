import cv2

img1 = cv2.imread('me.png')
img2 = cv2.imread('yz1.png')

totalImg = cv2.add(img1, img2)

#print('img1', img1[160, 80])
#print('img2', img2[160, 80])
#print('totalImg', totalImg[160, 80])

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('totalimg', totalImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
