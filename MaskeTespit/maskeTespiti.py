# OpenCV ile Maske Tespiti

import cv2
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gri, 1.1, 7)

    if len(faces) == 0:
        cv2.putText(frame, "yuz tespit edilemedi", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gri = gri[y:y+h, x:x+w] # yakınlaşma işlemi yapıldı
            mouth = mouth_cascade.detectMultiScale(roi_gri, 1.4, 12) # 12 defa iterasyon yapılsın
            # yüzde 1 defa ağız şekline benzer bir şey bulunca yazma 12 defa bulunca yaz
            i = 0
            if len(mouth) == 0:
                cv2.putText(frame, "maske var", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                for x1, y1, w1, h1 in mouth:
                    if i == 0:
                        i = i+1
                        cv2.rectangle(frame, (x1+x, y1+x), (x1 + w1 + x, y1 + h1 + y), (111, 111, 111), 3)
                        cv2.putText(frame, "maske yok", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                    else:
                        pass

    cv2.imshow("a", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
