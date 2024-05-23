import cv2
import numpy as np

img = cv2.imread("balon.jpg", 0)

sat, sut = img.shape
# print(sat)
# print(sut)

m = cv2.getRotationMatrix2D((sut/2, sat/2), 180, 1)
d = cv2.warpAffine(img, m, (sut, sat))

cv2.imshow("resim", d)
cv2.waitKey(0)
cv2.destroyAllWindows()
