import cv2
import numpy as np

canvas = np.zeros((600, 600, 3), np.uint8) + 255

f1 = cv2.FONT_ITALIC
f2 = cv2.FONT_HERSHEY_PLAIN
f3 = cv2.CAP_AVFOUNDATION

cv2.putText(canvas, "Merhaba", (30, 200), f3, 3, (255, 0, 0), cv2.LINE_AA)

cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
