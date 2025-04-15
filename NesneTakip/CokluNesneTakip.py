# Çoklu Nesne Takip Uygulaması

import cv2
print(cv2.__version__)
trackers = ["BOOSTING", "MIL", "CSRT", "KCF", "TLD", "MEDIANFLOW", "MOSSE"]

i = 0

cap = cv2.VideoCapture("test.mp4")
ret, frame = cap.read()

if ret == False:
    print("video okunamadı")

boxes = []

while True:
    box = cv2.selectROI("tracker", frame)
    boxes.append(box)
    print("Çıkış için q, nesne seçimine devam etmek için bir tuşa basın")
    # seçtikten sonra önce enter'a sonra bir tuşa veya q'ya basınız
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

multi_tracker = cv2.legacy.MultiTracker_create()

for box in boxes:
    multi_tracker.add(cv2.legacy.TrackerBoosting_create(), frame, box)

print(boxes)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video bitti ya da kare alınamadı.")
        break

    success, multiBoxes = multi_tracker.update(frame)

    for i, bbox in enumerate(multiBoxes):
        (x, y, w, h) = [int(j) for j in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Takip", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()