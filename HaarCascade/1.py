# Haar Cascade Resim Uzerinden Yüz Tespiti

import cv2

# img = cv2.imread("yuz5.jpg")
# img = cv2.imread("yuz6.jpeg")
img = cv2.imread("yuz7.jpeg")

yuz = cv2.CascadeClassifier("frontalface.xml")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = yuz.detectMultiScale(gri, 1.3, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("1", img)

cv2.waitKey()
cv2.destroyAllWindows()
