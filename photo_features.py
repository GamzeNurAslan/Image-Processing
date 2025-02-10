import cv2

img = cv2.imread('x.png')
img_gray = cv2.imread('x.png', 0)

#item
img.item(y, x, colour)
print('Blue', img.item(10, 10, 0))
print('Green', img.item(10, 10, 1))
print('Red', img.item(10, 10, 2))
print(img[300, 250])

#-----------------------------------------------#

#itemset
img.itemset((y, x, colour), value)
img[10, 10, 0] = 0

for y in range(50):
    for x in range(50):
        img[y, x, 0] = 0
        img[y, x, 1] = 0
        img[y, x, 2] = 0

#for y in range(50):
#    for x in range(50):
#       img[y, x] = [0, 0, 0]

cv2.imshow('Profil', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------#

#shape
print(img.shape)
print(img_gray.shape)

y, x, c = img.shape
print('y:', y, 'x:', x, 'c:', c)

#--------------------------------------------#

#size
print(img.size)
print(img_gray.size)

#--------------------------------------------#

#datatype
print(img.dtype)

#-------------------------------------------#

#ROI
#roi = img[y1:y2, x1:x2]
roi = img[645:645, 485:485] 

cv2.imshow('goz', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

#------------------------------------------#

#renk filtresi
img[:, :, 0] = 0 #yellow
img[:, :, 1] = 0 #red
img[:, :, 2] = 0 #black

img[:, :, 0] = 255 
img[:, :, 1] = 255 #white
img[:, :, 2] = 255

cv2.imshow('Profil', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


