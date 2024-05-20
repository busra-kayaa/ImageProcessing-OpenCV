import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # varsayılan kameradan video yakalama
dosya_adi = "C:/Video/1.avi"
codec = cv2.VideoWriter.fourcc('W', 'M', 'V', '2')
framerate = 30
resolution = (640, 480)
output = cv2.VideoWriter(dosya_adi, codec, framerate, resolution)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.flip(frame, 1)
    output.write(frame)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # q ya basınca kamera kapanır
        break

    cv2.waitKey(30)
output.release()
cap.release()
cv2.destroyAllWindows()
