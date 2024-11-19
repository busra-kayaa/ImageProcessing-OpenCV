# Haar Cascade Video Üzerinden Vücut Algılama
import cv2

cap = cv2.VideoCapture("insanlar.mp4")
vucud = cv2.CascadeClassifier("fullBody.xml")

while True:
    ret, frame = cap.read()

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = vucud.detectMultiScale(gri, 1.1, 4)

    for x, y, w, h in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("1", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()