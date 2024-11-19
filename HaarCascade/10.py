# OpenCV Haar Cascade Video Üzerinden Araç Tespiti

import cv2

cap = cv2.VideoCapture("araba.mp4")
araba = cv2.CascadeClassifier("cars.xml")


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    if not ret:
        print("Video sona erdi veya kare okunamadı.")
        break

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = araba.detectMultiScale(gri, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))

    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Arac Tespiti", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
