import cv2
img = cv2.imread("balon.jpg")

roi = img[400:500, 300:480]

cv2.imshow("resim", img)
cv2.imshow("roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ROI: ilgi alanı, resim üstünde istenilen ya da ilgilenilen alan
