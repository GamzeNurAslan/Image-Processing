import cv2

img1 = cv2.imread('me.png')
img2 = cv2.imread('yz1.png')

totalWeightedImg = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('totalWeightedImg', totalWeightedImg)

print('img1', img1[160, 80])
print('img2', img2[160, 80])
print('totalImg', totalWeightedImg[160, 80])

cv2.waitKey(0)
cv2.destroyAllWindows()

#Aritmetik Toplama Örneğidir"
