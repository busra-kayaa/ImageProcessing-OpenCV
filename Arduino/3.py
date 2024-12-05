# OpenCV El Hareketi ile Led Yakma Uygulaması
import cv2
import numpy as np
import math
import serial

# Arduino ile bağlantı kur
arduino = serial.Serial('COM8', 9600)  # Arduino'nun bağlı olduğu portu buraya yazın

# Web kamerası
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)  # Aynalama
    kernel = np.ones((5, 5), np.uint8)  # Daha büyük bir kernel

    # ROI: Algılama yapılacak alan
    roi = frame[75:300, 75:300]

    cv2.rectangle(frame, (75, 75), (300, 300), (0, 255, 0), 2)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Cilt rengini maskeleme için daha hassas HSV aralığı
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Cilt rengini maskele
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Maskeyi dilate et ve erozyona uğrat (morfolojik işlemler)
    mask = cv2.dilate(mask, kernel, iterations=2)  # Dilation
    mask = cv2.erode(mask, kernel, iterations=1)   # Erosion
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Kontur bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))  # En büyük konturu seç

        # Kavrama alanı hesaplama
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Konveks hull (dış hatları kapsama)
        hull = cv2.convexHull(cnt)
        # Parmak çevresini çiz
        cv2.drawContours(roi, [hull], 0, (0, 255, 0), 2)  # Parmak çevresini yeşil çizgiyle çiz

        # Çıkıntılar (defects) bulma
        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)

        points = []  # Parmak aralarındaki noktalar

        l = 0  # Parmak sayısı

        # Defect'ler üzerinden geçerek parmak aralarını bulma
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])

                # Üçgen kenar uzunlukları
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

                # Üçgen alanı hesaplama (Heron's formula)
                s = (a + b + c) / 2
                ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

                # Açıyı hesaplama
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                # Eğer açı < 90 ise bu bir parmak olabilir
                if angle <= 90 and d > 30:
                    l += 1
                    # Parmak aralarını nokta ile işaretle
                    cv2.circle(roi, far, 8, (255, 0, 0), -1)  # Noktayı çiz
                    points.append(far)  # Noktayı listeye ekle

            l += 1  # Başparmak için

        # Parmak sayısını yazdır
        cv2.putText(frame, str(l), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Parmak sayısını Arduino'ya gönder
        arduino.write(f"{l}\n".encode())

    # Çıktıyı göster
    cv2.imshow('Frame', frame)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video kaynağını serbest bırak
vid.release()
cv2.destroyAllWindows()

# Arduino Kodları
"""
int ledPins[] = {2, 3, 4, 5, 6}; // LED'lerin bağlı olduğu pinler
int ledCount = 5;                // Maksimum LED sayısı
String inputString = "";         // Gelen seri veri

void setup() {
  Serial.begin(9600);            // Seri iletişimi başlat
  for (int i = 0; i < ledCount; i++) {
    pinMode(ledPins[i], OUTPUT); // LED pinlerini çıkış olarak ayarla
    digitalWrite(ledPins[i], LOW); // Başlangıçta tüm LED'ler kapalı
  }
}

void loop() {
  // Seri porttan veri alındığında işle
  if (Serial.available()) {
    char inChar = (char)Serial.read(); // Karakteri oku
    if (inChar == '\n') {             // Satır sonu geldiğinde işle
      int fingerCount = inputString.toInt(); // Gelen veriyi sayıya çevir

      // Eğer gelen veri geçerli değilse, LED'leri kapalı tut
      if (fingerCount <= 0 || fingerCount > ledCount) {
        fingerCount = 0; // Geçersiz sayı durumunda LED'leri kapat
      }

      // LED'leri kontrol et
      controlLEDs(fingerCount);

      // Gelen veriyi sıfırla
      inputString = "";
    } else {
      inputString += inChar; // Karakterleri birleştir
    }
  }
}

// Gelen parmak sayısına göre LED'leri kontrol eden fonksiyon
void controlLEDs(int count) {
  // Önce tüm LED'leri kapat
  for (int i = 0; i < ledCount; i++) {
    digitalWrite(ledPins[i], LOW);
  }

  // Parmak sayısına göre LED'leri yak
  for (int i = 0; i < count; i++) {
    digitalWrite(ledPins[i], HIGH);
  }
}
"""