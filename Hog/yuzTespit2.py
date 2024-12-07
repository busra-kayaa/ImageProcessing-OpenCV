# Histogram of Oriented Gradients - HOG ile Yüz Tespiti

import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    facelocs = face_recognition.face_locations(frame, model="hog")

    for index, faceloc in enumerate(facelocs):
        toplefty, bottomrightx, bottomrighty, topleftx = faceloc

        detectedFace = frame[toplefty:bottomrighty, topleftx:bottomrightx]

        cv2.rectangle(frame, (topleftx, toplefty), (bottomrightx, bottomrighty), (255, 0, 0), 3)

        cv2.imshow("kesilen", detectedFace)
        cv2.imshow("orj", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()