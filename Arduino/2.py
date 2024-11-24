# Yüz Tanıdığında Arduino ile Led Yakma
import cv2
import serial
import time

arduino = serial.Serial('COM8', 9600)

cap = cv2.VideoCapture(0)
yuz = cv2.CascadeClassifier("frontalface.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = yuz.detectMultiScale(gri, 1.2, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        arduino.write(b'1')
        time.sleep(0.5)

    cv2.imshow("1", frame)
    arduino.write(b'0')

    if cv2.waitKey(50) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# ARDUİNO KODU
""" 
int datafromUser = 0;
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode (led, OUTPUT); // Arduino'nun D10 pini çıkış olarak ayarlanı
  Serial.begin(9600); // Seri haberleşme başlatılır
}

void loop() {

  Serial.println("Arduino Çalışıyor...");
  delay(1000);

  // put your main code here, to run repeatedly:
  if ( Serial.available() > 0) // Seri portta veri varsa
  {
    datafromUser = Serial.read(); // Gelen veriyi oku
  }

  if (datafromUser == '1')
  {
    digitalWrite(led, HIGH); // LED'i aç
  }

  else if (datafromUser == '0')
  {
    digitalWrite (led, LOW); // LED'i kapat
  }

}
"""