import cv2
import numpy as np

img1 = cv2.imread("blackWhite.jpg")
img2 = cv2.imread("circleBlack.jpg")

print(img1.shape)
print(img2.shape)

# Eğer img1 ve img2 boyutları farklıysa, aynı boyuta getirin
img1 = cv2.resize(img1, (638, 650))  # width ve height uygun değerlerle değiştirilmelidir
img2 = cv2.resize(img2, (638, 650))
"""
bit_and = cv2.bitwise_and(img1, img2)
cv2.imshow("bir", img1)
cv2.imshow("iki", img2)
cv2.imshow("and", bit_and)
"""
bit_or = cv2.bitwise_or(img1, img2)
cv2.imshow("bir", img1)
cv2.imshow("iki", img2)
cv2.imshow("or", bit_or)
# 0 siyah, beyaz 1
"""
bit_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow("bir", img1)
cv2.imshow("iki", img2)
cv2.imshow("xor", bit_xor)


bit_not1 = cv2.bitwise_not(img1, img2)
bit_not2 = cv2.bitwise_not(img2, img1)
cv2.imshow("bir", img1)
cv2.imshow("iki", img2)
cv2.imshow("not1", bit_not1)
cv2.imshow("not2", bit_not2)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
