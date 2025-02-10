import cv2

img = cv2.imread('yz.png')
print('Original size ->', img.shape)

#imgResized = cv2.resize(img, (150, 250))
#print('Resized size ->', imgResized.shape)
#cv2.imshow('resized', imgResized)

y, x, c = img.shape
imgResized = cv2.resize(img, (x+x//2, y+y//2))
print('Resized size ->', imgResized.shape)
cv2.imshow('resized', imgResized)

cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
