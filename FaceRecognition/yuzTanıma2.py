#  OpenCV Face_Recognition ile Çoklu Kişi Tanıma
import cv2
import dlib
import face_recognition


detector =dlib.get_frontal_face_detector()

busra = face_recognition.load_image_file("busra.jpg")
busra_enc = face_recognition.face_encodings(busra)[0]

omer = face_recognition.load_image_file("omer.jpg")
omer_enc = face_recognition.face_encodings(omer)[0]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    face_loc = []
    faces = detector(frame)

    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right()
        h = face.bottom()
        face_loc.append((y, w, h, x))

   # face_loc = face_recognition.face_locations(frame)
    face_encoding = face_recognition.face_encodings(frame, face_loc)
    i = 0
    for face in face_encoding:
        y, w, h, x = face_loc[i]
        sonuc = face_recognition.compare_faces([busra_enc], face)
        sonuc1 = face_recognition.compare_faces([omer_enc], face)

        # print(sonuc)
        if sonuc[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "Busra", (x, h+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        elif sonuc1[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "OMERCIK", (x, h+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        else:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "Yabanci", (x, h+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("1", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
