# pytesseract ile Plaka Okuma
import cv2
import numpy as np
import pytesseract
import imutils

# Tesseract yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Görüntüyü yükle ve griye çevir
img = cv2.imread("plaka3.png")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültü azaltma filtresi
filtre = cv2.bilateralFilter(gri, 7, 200, 200)

# Kenar tespiti
kose = cv2.Canny(filtre, 40, 200)

# Kontur bulma
kontur, a = cv2.findContours(kose, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours((kontur, a))
cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:10]

ekran = None

# Dört kenarlı plaka bölgesini bul
for i in cnt:
    eps = 0.018 * cv2.arcLength(i, True)
    aprx = cv2.approxPolyDP(i, eps, True)
    if len(aprx) == 4:
        ekran = aprx
        break

# Maske oluştur ve bölgeyi çıkar
if ekran is not None:
    maske = np.zeros(gri.shape, np.uint8)
    yeniMaske = cv2.drawContours(maske, [ekran], 0, (255, 255, 255), -1)
    yazi = cv2.bitwise_and(img, img, mask=maske)

    cv2.imshow("YeniMaske", yeniMaske)
    cv2.imshow("Yazi", yazi)

    # Plaka bölgesini kırp
    (x, y) = np.where(maske == 255)
    (ustx, usty) = (np.min(x), np.min(y))
    (altx, alty) = (np.max(x), np.max(y))
    kirp = gri[ustx:altx + 1, usty:alty + 1]

    # OCR ile metni al
    config = "--psm 6"  # Kısa metinler için
    text = pytesseract.image_to_string(kirp, lang="eng", config=config)
    print("Plaka Metni:", text)

    # Görüntüleri göster
    cv2.imshow("Kirpilan Plaka", kirp)
else:
    print("Plaka konturu bulunamadı!")

# Ek görüntüleri göster
cv2.imshow("Orijinal", img)
cv2.imshow("Gri", gri)
cv2.imshow("Filtre", filtre)
cv2.imshow("Kose", kose)

cv2.waitKey(0)
cv2.destroyAllWindows()


