import cv2
cap = cv2.VideoCapture("Robot.mp4")  # bilgisayar üzerinden bir dosyadan çekeceksek dosya konumunu yazmalıyız

while True:
    ret, frame = cap.read()
    if ret == 0:
        break

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q ya basınca kamera kapanır
        break

cap.release()
cv2.destroyAllWindows()
