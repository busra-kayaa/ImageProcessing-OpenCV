# OpenCV Python ile Arduino Kontrolü

import serial
import time

arduino = serial.Serial('COM8', 9600)
time.sleep(2)

print("Enter 1 to turn ON LED and 0 to turn OFF LED")

while 1:
    datafromUser = input()

    if datafromUser == '1':
        arduino.write(b'1')
        print("LED turned ON")

    elif datafromUser == '0':
        arduino.write(b'0')
        print("LED turned OFF")

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