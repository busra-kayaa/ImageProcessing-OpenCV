import cv2
import numpy as np

# img = cv2.imread("ucgen.png")
img = cv2.imread("openCV.png")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gri = np.float32(gri)
corner = cv2.goodFeaturesToTrack(gri, 100, 0.01, 10)

corner = np.intp(corner)

for c in corner:
    x, y = c.ravel()

    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


cv2.imshow("u", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
