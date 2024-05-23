import cv2
import numpy as np

img = cv2.imread("resim.jpg")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gri, 100, 200, cv2.THRESH_BINARY)  # 0-1e çeviriyor, 0 lar siyahı 1ler beyazı

cont, a = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(cont)

cv2.drawContours(img, cont, -1, (0, 255, 0), 2)
# cont: Çizilecek olan konturların listesi. Her bir kontur, bir dizi noktadan oluşan bir liste olarak temsil edilir.
# -1: Çizilecek olan konturların indeksini belirtir.
# -1 değeri, tüm konturların çizilmesini sağlar.
# 2: Kontur çizgilerinin kalınlığını belirtir. Bu sayı arttıkça çizgiler kalınlaşır.
cv2.imshow("1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

