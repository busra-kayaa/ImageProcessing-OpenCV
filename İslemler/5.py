import cv2
import numpy as np

img1 = cv2.imread("bilateral.jpg")
img2 = cv2.imread("filter.jpg")
img3 = cv2.imread("median.jpg")

blr = cv2.blur(img2, (15, 15))
gb = cv2.GaussianBlur(img2, (15, 15), cv2.BORDER_DEFAULT)

mb = cv2.medianBlur(img3, 7)

b = cv2.bilateralFilter(img1, 9, 75, 75)

cv2.imshow("orj", img1)
cv2.imshow("blur", blr)
cv2.imshow("gb", gb)
cv2.imshow("mb", mb)
cv2.imshow("b", b)


cv2.waitKey(0)
cv2.destroyAllWindows()
