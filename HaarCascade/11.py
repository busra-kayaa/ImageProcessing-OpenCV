# Haarcascade ile Tespit Edilen Yüzün Merkezine Fare İmleci Konumlandırma

import cv2
import pyautogui

# Video ve cascade dosyasını yükleme
cap = cv2.VideoCapture("frontFace1.mp4")
yuz = cv2.CascadeClassifier("frontalface.xml")

screen_width, screen_height = pyautogui.size()

video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow("1", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("1", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()

    if not ret:
        break  # Video bittiğinde döngüden çık

    # Gri tonlamaya çevir
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti
    faces = yuz.detectMultiScale(gri, 1.2, 4)

    # Tespit edilen yüzlerin etrafına dikdörtgen çiz
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        center_x = x + w // 2
        center_y = y + h // 2

        cv2.circle(frame, (center_x, center_y), 3, (0, 255, 0), -1)
        translated_x = center_x * (screen_width / video_width)
        translated_y = center_y * (screen_height / video_height)
        pyautogui.moveTo(translated_x, translated_y)

    # Kareyi görüntüle
    cv2.imshow("1", frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()