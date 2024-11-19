# Haar Cascade Video Uzerinden Yüz Tespiti

import cv2

# Video ve cascade dosyasını yükleme
cap = cv2.VideoCapture("frontFace2.mp4")
yuz = cv2.CascadeClassifier("frontalface.xml")

while True:
    ret, frame = cap.read()

    if not ret:
        break  # Video bittiğinde döngüden çık

    # Videoyu yeniden boyutlandırma
    frame = cv2.resize(frame, (640, 480))  # Örneğin 640x480 boyutuna ayarlama

    # Gri tonlamaya çevir
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti
    faces = yuz.detectMultiScale(gri, 1.2, 4)

    # Tespit edilen yüzlerin etrafına dikdörtgen çiz
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Kareyi görüntüle
    cv2.imshow("Yüz Tespiti", frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()