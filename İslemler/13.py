# OpenCV Convex Hull ile Dış Bükey Alan ve Çevre Hesaplama
import cv2
import numpy as np

img = cv2.imread("yildiz.jpg")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

a, thresh = cv2.threshold(gri, 125, 255, cv2.THRESH_BINARY)
contur, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []
for i in range(len(contur)):
    hull.append(cv2.convexHull(contur[i], False))

tuval = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contur)):
    cv2.drawContours(tuval, contur, i, (255, 0, 0), 3, 8, hier)
    cv2.drawContours(tuval, hull, i, (0, 255, 0), 1, 8)

cnt = hull[0]
print(cnt)

M = cv2.moments(cnt)
print(M)

alan = cv2.contourArea(cnt)
print(alan)
print(M['m00'])

cevre = cv2. arcLength(cnt, True)
print(cevre)

cv2.imshow("a", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

