# Face_Recognition ile Resim Üzerinde Birden Fazla Kişiyi Tanıma

import cv2
import face_recognition

# İlk kişiyi yükle ve kodlamasını al
kisi1 = face_recognition.load_image_file("tarkan.jpg")
kisi1encodings = face_recognition.face_encodings(kisi1)[0]

# İkinci kişiyi yükle ve kodlamasını al
kisi2 = face_recognition.load_image_file("halukBilginer.png")
kisi2encodings = face_recognition.face_encodings(kisi2)[0]

# Kodlama ve isim listesi
encodingslist = [kisi1encodings, kisi2encodings]
namelist = ["Tarkan", "Haluk Bilginer"]

# Test resmi yükle
"""""
image = cv2.imread("tarkan1.jpg")
test1 = face_recognition.load_image_file("tarkan1.jpg")

image = cv2.imread("halukBilginer2.jpg")
test1 = face_recognition.load_image_file("halukBilginer2.jpg")

image = cv2.imread("ilberOrtayli.jpg")
test1 = face_recognition.load_image_file("ilberOrtayli.jpg")
"""""

image = cv2.imread("birlikte.png")
test1 = face_recognition.load_image_file("birlikte.png")

# Test resmindeki yüzleri tespit et
facelocations = face_recognition.face_locations(test1)
faceencodings = face_recognition.face_encodings(test1, facelocations)

# Yüzleri çerçeveleme ve isimlendirme
for faceloc, faceencoding in zip(facelocations, faceencodings):
    ustsoly, altsagx, altsagy, ustsolx = faceloc
    matchFaces = face_recognition.compare_faces(encodingslist, faceencoding)

    name = "Bilinmeyen Kisi"

    if True in matchFaces:
        matchedindex = matchFaces.index(True)
        name = namelist[matchedindex]

    # Çerçeve ve metin ekleme
    cv2.rectangle(image, (ustsolx, ustsoly), (altsagx, altsagy), (255, 0, 0), 2)
    cv2.putText(image, name, (ustsolx, ustsoly - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    print(name)

# Sonucu göster
cv2.imshow("Sonuc", image)
cv2.waitKey(0)
cv2.destroyAllWindows()