#  OpenCV Haar Cascade WebCam Üzerinden Yüz Tespiti
import cv2

cap = cv2.VideoCapture(0)
yuz = cv2.CascadeClassifier("frontalface.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = yuz.detectMultiScale(gri, 1.2, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("1", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()