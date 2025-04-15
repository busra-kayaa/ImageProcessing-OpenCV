# Eğitilmiş Model ile Nesne Takip Uygulaması GOTURN Algoritması

import cv2

tracker = cv2.TrackerGOTURN_create()
cap = cv2.VideoCapture("test.mp4")
ret, frame = cap.read()

box = cv2.selectROI("Takip Başlangıcı", frame)
ret = tracker.init(frame, box)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video oynatılamadı.")
        break

    success, box = tracker.update(frame)

    if success:
        (x, y, w, h) = [int(i) for i in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    else:
        cv2.putText(frame, "❌ Nesne kayboldu", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Algoritma ismini farklı yere yaz
    cv2.putText(frame, "Goturn Algoritmasi", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Takip", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
