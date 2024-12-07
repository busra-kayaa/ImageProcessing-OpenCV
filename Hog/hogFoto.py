# Histogram of Oriented Gradients - HOG Uygulaması

import cv2
from skimage.feature import hog
from skimage import exposure

image = cv2.imread("Eileen_Collins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, hogimage = hog(gray, visualize=True)
rescaled = exposure.rescale_intensity(hogimage, in_range=(0, 10))

cv2.imshow("re", rescaled)
cv2.imshow("hog", hogimage)
cv2.imshow("org", image)

cv2.waitKey(0)
cv2.destroyAllWindows()