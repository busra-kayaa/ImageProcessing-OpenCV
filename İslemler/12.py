import cv2
import numpy as np

img = cv2.imread("yildiz.jpg")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gri, 75, 200, cv2.THRESH_BINARY)
contur, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.findContours fonksiyonu, bir görüntü üzerindeki konturları tespit etmek için kullanılan bir OpenCV fonksiyonudur.
# thresh: Kontur tespiti yapılacak olan eşiklenmiş (thresholded) görüntü.
# Kontur tespiti genellikle siyah-beyaz (binary) bir görüntü üzerinde gerçekleştirilir.
# Fonksiyonun çıktısı olarak, cont değişkenine kontur listesi ve h değişkenine hiyerarşik yapı bilgisi atanır.

print(contur)
# Konveks Kapalı Çizgilerin Hesaplanması:
h = list()
for i in range(len(contur)):
    h.append(cv2.convexHull(contur[i], False))
    # cv2.convexHull fonksiyonu, bir konturun konveks kapalı çizgisini oluşturur.
    # Bu çizgi, orijinal konturu çevreleyen en küçük konveks şekli ifade eder.

# Görüntü İçin Bir Temel Oluşturma:
z = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# Konturların ve Konveks Kapalı Çizgilerin Çizilmesi:
for i in range(len(contur)):
    cv2.drawContours(z, contur, i, (255, 0, 0), 3, 8)  # Konturun mavi renkte çizilmesi
    cv2.drawContours(z, h, i, (0, 255, 0), 1, 8)

cv2.imshow("resim", z)
cv2.waitKey(0)
cv2.destroyAllWindows()

