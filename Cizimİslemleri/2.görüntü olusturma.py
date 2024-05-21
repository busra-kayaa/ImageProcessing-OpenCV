import cv2
import numpy as np
"""""
img = np.zeros((20, 20, 3), np.uint8) + 255
img[0, 0] = (0, 0, 0)
img[0, 1] = (50, 0, 0)
img[0, 2] = (100, 0, 0)
img[0, 3] = (150, 0, 0)
img[0, 4] = (200, 0, 0)
img[0, 5] = (250, 0, 0)
# Görüntünün belirli piksellerine renk değerleri atayarak görüntüde renk değişiklikleri yapar. 
"""""
img = np.zeros((20, 20), np.uint8) + 255
# İlk olarak, 20x20 boyutunda bir NumPy dizisi oluşturulur. Bu dizi, np.zeros fonksiyonu ile başlatılır
#  ve ardından + 255 eklenerek tüm piksellerin değeri 255'e (beyaz) ayarlanır.

img[0, 0] = 255
img[0, 1] = 200
img[0, 2] = 150
img[0, 3] = 100
img[0, 4] = 50
img[0, 5] = 0

# İlk satırın belirli piksellerine gri tonları atanır.
#  np.uint8 veri tipi, her bir pikselin 8 bitlik bir tamsayı ile temsil edildiği anlamına gelir.

img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
# cv2.resize: Bu fonksiyon, bir görüntüyü belirli bir boyuta yeniden boyutlandırmak için kullanılır.
# img: Yeniden boyutlandırılacak olan görüntü.
# (300, 300): Hedef boyut. Burada, görüntünün yeni genişlik ve yüksekliği 500 piksel olacak şekilde belirlenmiştir.
# interpolation=cv2.INTER_AREA: Yeniden boyutlandırma işlemi sırasında kullanılacak interpolasyon yöntemini belirler.
# cv2.INTER_AREA, görüntüyü küçültürken yüksek kalite sağlamak için kullanılan bir interpolasyon yöntemidir.q

cv2.imshow("pencere", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
