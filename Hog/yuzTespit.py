# Histogram of Oriented Gradients - HOG ile Yüz Tespiti

import cv2
import face_recognition

image = cv2.imread("Ataturk1930s.jpg")

facelocs = face_recognition.face_locations(image, model="cnn")

for index, faceloc in enumerate(facelocs):
    toplefty, bottomrightx, bottomrighty, topleftx = faceloc

    detectedFace = image[toplefty:bottomrighty, topleftx:bottomrightx]

    cv2.rectangle(image, (topleftx, toplefty), (bottomrightx, bottomrighty), (255, 0, 0), 3)

    cv2.imshow("kesilen", detectedFace)
    cv2.imshow("orj", image)

cv2.waitKey(0)
cv2.destroyAllWindows()