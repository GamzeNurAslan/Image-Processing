import cv2

vid = cv2.VideoCapture(0) #Sıfır olmasının sebebi bilgisayarın kendi kamerasına erişimini sağlar

while True:
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    kInp = cv2.waitKey(1) #WaitKey'in 0 olması demek anlık fotoğraf göstermesi demek iken
                             #1000 olursa saniyede bir görüntü elde etmemizi sağlar.


    if kInp == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
