#  OpenCV Haar Cascade Resim Üzerinden Araç Tespiti

import cv2

img = cv2.imread("car1.jpg")
img = cv2.resize(img, (400, 400))

araba = cv2.CascadeClassifier("cars.xml")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = araba.detectMultiScale(gri, 1.2, 1)

for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()