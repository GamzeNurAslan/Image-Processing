import cv2

img = cv2.imread('x.png')
#Resim zaten gri formata döndürleceği için üstteki kod parçacığı gibi değil de biz de gri formata getirilmesini yazabiliriz.
img = cv2.imread("x.png", cv2.IMREAD_GRAYSCALE)
#Ya da gri yazmak yerine sayısal karşılığını yazabiliriz.
img = cv2.imread("x.png", 0)

cv2.imshow('Profil', img)

kInp = cv2.waitKey(0)
print(kInp)

"""if kInp == 97:
    print('a tuşuna basıldı')
else:
    print('başka bir tuşa basıldı')"""

#Eğer üstteki gibi yazmak istemiyorsam şu şekilde de yazabilirim:

if kInp == ord('a'):
    print('a tuşuna basıldı')
else:
    print('başka bir tuşa basıldı')

cv2.destroyAllWindows()
