import cv2
import numpy as np

img = cv2.imread("balon.jpg")

img[200, 300, 0] = 0
print(img[200, 300])

blue = img.item(150, 150, 0)
print(blue)

img.itemset((150, 150, 0), 200)
print(img[150, 150])
"""
renk = img[450, 300]
print(renk)
# print(img.shape)

blue = img[450, 300, 0]
print("blue", blue)

green = img[450, 300, 1]
print("green", green)

red = img[450, 300, 2]
print("red", red)
"""

cv2.imshow("ballon", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


