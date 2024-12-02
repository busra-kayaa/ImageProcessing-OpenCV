# OpenCV Face_Recognition ile Tanınan Kişiyi Tarihi ile Veritabanına Ekleme
import cv2
import dlib
import face_recognition

from datetime import datetime

import sqlite3
con = sqlite3.connect("yuzTaninan.db")
cursor = con.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS kisiler (ad TEXT, zaman DATETIME)")
    con.commit()

tablo()

def ekle(isim, tarih):
    tarih = datetime.now().isoformat()
    cursor.execute("INSERT INTO kisiler VALUES (?, ?)", (isim, tarih))
    con.commit()

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

            ekle("Busra", datetime.now())

        elif sonuc1[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "Omo", (x, h+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            ekle("Omer", datetime.now())

        else:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "Yabanci", (x, h+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            ekle("Yabanci", datetime.now())

    cv2.imshow("1", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()