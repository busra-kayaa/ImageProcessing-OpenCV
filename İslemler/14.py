# Şekil Algılama
import cv2
import numpy as np

img = cv2.imread("sekil.png")
font = cv2.FONT_HERSHEY_COMPLEX
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, thresh = cv2.threshold(gri, 200, 300, cv2.THRESH_BINARY)
cont, b = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in cont:
    e = 0.01 * cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, e, True)
    cv2.drawContours(img, [approx], 0, 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(approx)
    print(len(approx))

    if len(approx) == 3:
        cv2.putText(img, "ucgen", (x, y), font, 1, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "kare", (x, y), font, 1, 1, (0))
    else:
        cv2.putText(img, "daire", (x, y), font, 1, 1, (0))


cv2.imshow("resim", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

