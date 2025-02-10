import cv2

img = cv2.imread('yz.png')

"""imgCropped = img[160:200, :150]
   cv2.imshow('cropped', imgCropped)"""

y, x, c = img.shape
imgCropped1 = img[0:y//2, 0:x//2]
cv2.imshow('cropped1', imgCropped1)

imgCropped2 = img[0:y//2, x//2:x]
cv2.imshow('cropped2', imgCropped2)

imgCropped3 = img[y//2:y, 0:x//2]
cv2.imshow('cropped3', imgCropped3)

imgCropped4 = img[y//2:y, x//2:x]
cv2.imshow('cropped4', imgCropped4)
cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
