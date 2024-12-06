# Opencv trackbar Üzerinde Nesne Algılama

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def fonks(x):
    pass

cv2.namedWindow("bar")
cv2.resizeWindow("bar", 600, 600)

cv2.createTrackbar("alt-h", "bar", 0, 180, fonks)
cv2.createTrackbar("alt-s", "bar", 0, 255, fonks)
cv2.createTrackbar("alt-v", "bar", 0, 255, fonks)

cv2.createTrackbar("ust-h", "bar", 0, 180, fonks)
cv2.createTrackbar("ust-s", "bar", 0, 255, fonks)
cv2.createTrackbar("ust-v", "bar", 0, 255, fonks)

cv2.setTrackbarPos("ust-h",  "bar", 150)
cv2.setTrackbarPos("ust-s",  "bar", 200)
cv2.setTrackbarPos("ust-v",  "bar", 200)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    alt_h = cv2.getTrackbarPos("alt-h", "bar")
    alt_s = cv2.getTrackbarPos("alt-s", "bar")
    alt_v = cv2.getTrackbarPos("alt-v", "bar")

    ust_h = cv2.getTrackbarPos("ust-h", "bar")
    ust_s = cv2.getTrackbarPos("ust-s", "bar")
    ust_v = cv2.getTrackbarPos("ust-v", "bar")

    cv2.setTrackbarPos("ust-h", "bar", 151)
    cv2.setTrackbarPos("ust-s", "bar", 255)
    cv2.setTrackbarPos("ust-v", "bar", 232)

    cv2.setTrackbarPos("alt-h", "bar", 0)
    cv2.setTrackbarPos("alt-s", "bar", 140)
    cv2.setTrackbarPos("alt-v", "bar", 146)

    alt_renk = np.array([alt_h, alt_s, alt_v])
    ust_renk = np.array([ust_h, ust_s, ust_v])

    mask = cv2.inRange(frame_hsv, alt_renk, ust_renk)

    cv2.imshow("o", frame)
    cv2.imshow("m", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

    if np.any(mask >= 255):
        print("Kirmizi nesne algilandi")


cap.release()
cv2.destroyAllWindows()

