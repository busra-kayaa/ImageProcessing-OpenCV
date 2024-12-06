# Trafikte Geçen Araç Sayısı Hesaplama

import cv2

# Video ve arka plan ayarı
vid = cv2.VideoCapture("traffic.mp4")
backsub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=False)

car_positions = []  # Araç merkez noktalarını saklamak için bir liste
c = 0  # Toplam geçen araç sayısı

while True:
    ret, frame = vid.read()
    if not ret:
        break

    fgmask = backsub.apply(frame)
    fgmask = cv2.medianBlur(fgmask, 5)  # Gürültü azaltma
    cv2.line(frame, (400, 175), (650, 175), (0, 255, 0), 2)  # Geçiş çizgisi üst
    cv2.line(frame, (400, 275), (650, 275), (0, 255, 0), 2)  # Geçiş çizgisi alt

    contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    current_cars = []

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if w > 60 and h > 60:  # Minimum nesne boyutu
            cx, cy = x + w // 2, y + h // 2  # Araç merkez noktası
            current_cars.append((cx, cy))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Araç merkezlerini takip et ve bir kez say
    new_car_positions = []
    for (cx, cy) in current_cars:
        is_new_car = True
        for (px, py) in car_positions:
            if abs(cx - px) < 50 and abs(cy - py) < 50:  # Önceki çerçevedeki araçlarla eşleşme
                is_new_car = False
                break
        if is_new_car:
            new_car_positions.append((cx, cy))
            if 175 < cy < 275:  # Çizgi arasında geçiş kontrolü
                c += 1

    car_positions = current_cars  # Mevcut araçları takip listesi olarak güncelle

    # Araç sayısını ekrana yazdır
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"Cars: {c}", (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Foreground Mask", fgmask)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()