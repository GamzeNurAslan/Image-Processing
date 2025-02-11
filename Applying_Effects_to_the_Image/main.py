import cv2
import numpy as np

me = cv2.imread("me.png")
me[:,:,2] = 150
me[:,:,0] = 150

#Eğer sadece bir yerine uygulamak istiyorsak efekti :
#me[100:150,300:400,0] = 255

cv2.imshow("Fotoğrafım", me)

me[:,:,0] = 255

cv2.waitKey(0)
cv2.destroyAllWindows()
