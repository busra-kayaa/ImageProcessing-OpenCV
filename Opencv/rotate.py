# OpenCV Rotate İşlemleri
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare okunuyor.
    ret, frame = cap.read()

    # Görüntü yatay olarak aynalanıyor. Bu, kullanıcının hareketlerini aynadaki gibi görmesini sağlar.
    frame = cv2.flip(frame, 1)

    # Görüntüyü döndürmek için cv2.rotate kullanılıyor:
    # - cv2.ROTATE_90_CLOCKWISE: Görüntüyü saat yönünde 90 derece döndürür.
    # - cv2.ROTATE_90_COUNTERCLOCKWISE: Görüntüyü saat yönünün tersine 90 derece döndürür.
    # - cv2.ROTATE_180: Görüntüyü 180 derece döndürür (ters çevirir).

    # frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Döndürülen görüntü bir pencere içinde gösteriliyor.
    cv2.imshow("1", frame)

    if cv2.waitKey(5) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()