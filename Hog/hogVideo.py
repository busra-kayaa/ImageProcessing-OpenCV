import cv2
from skimage.feature import hog
from skimage import exposure

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, hogimage = hog(gray, visualize=True)
    rescaled = exposure.rescale_intensity(hogimage, in_range=(0, 10))

    cv2.imshow("hog", rescaled)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
