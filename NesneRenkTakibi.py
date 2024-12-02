# OpenCV Renk ile Nesne Tespiti

import cv2
import numpy as np
from collections import deque #verilerin merkezini saklamak için kullanılıyor.

'''
dq = deque(maxlen=3)

dq.append(5)
dq.append(4)
dq.appendleft(9)
print(dq)

dq.appendleft(12)
print(dq)

# max uzunluğu 3 yaptığımız için 3 değer alabiliyor.
dq.clear()
'''

buffer_size = 16
pts = deque(maxlen=buffer_size)

blueLower = (100, 150, 0)  # Mavi için alt sınır
blueUpper = (140, 255, 255)  # Mavi için üst sınır

cap = cv2.VideoCapture(0)

cap.set(3,960)
cap.set(4,480)

while True:
    success, imgOrginal = cap.read()

    if success:
        blurred = cv2.GaussianBlur(imgOrginal,(11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Penceresi",hsv)

        mask = cv2.inRange(hsv, blueLower, blueUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("Maskeli Pencere",mask)

        (contours, _) =cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        center = None

        if len(contours) >0:
            c = max(contours, key = cv2.contourArea)
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect

            s = "x:{}, y:{}, width:{}, height:{}, rotation:{} ".format(np.round(x),np.round(y),np.round(width), np.round(height), np.round(rotation))
            print(s)

            box = cv2.boxPoints(rect)
            box = np.int64(box)

            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            cv2.drawContours(imgOrginal,[box], 0,(0,255,255),2)
            cv2.circle(imgOrginal, center, 5, (255, 0, 0))


        pts.append(center)
        for i in range(1, len(pts)):
            if pts[i-1] is None or pts[i] is None:continue
            cv2.line(imgOrginal,pts[i-1], pts[i], (0, 255, 255), 3)

        cv2.imshow("original", imgOrginal)

        if cv2.waitKey(1) & 0xff == ord("q"):
            break