import cv2

image = cv2.imread('me.png')

meanFilter = cv2.blur(image, (3,3))
meanFilter2 = cv2.blur(image, (5,5))
meanFilter3 = cv2.blur(image, (7,7))

medianFilter=cv2.medianBlur(image,3)
medianFilter2=cv2.medianBlur(image,5)
medianFilter3=cv2.medianBlur(image,7)

gauss=cv2.GaussianBlur(image,(3,3), 0)
gauss2=cv2.GaussianBlur(image,(5,5), 0)
gauss3=cv2.GaussianBlur(image,(7,7), 0)

cv2.imshow('Original', image)
cv2.imshow('Mean Filter', meanFilter)
cv2.imshow('Mean Filter 5*5', meanFilter2)
cv2.imshow('Mean Filter 7*7', meanFilter3)

cv2.imshow('Median Filter', medianFilter)
cv2.imshow('Median Filter2', medianFilter2)
cv2.imshow('Median Filter3', medianFilter3)

cv2.imshow('gauss Filter', gauss)
cv2.imshow('gauss Filter2', gauss2)
cv2.imshow('gauss Filter3', gauss3)

cv2.waitKey(0)
cv2.destroyAllWindows()
