import cv2
# cismin merkezini bulma
img = cv2.imread("ucgenResmi.jpg")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ai, thresh = cv2.threshold(gri, 100, 200, cv2.THRESH_BINARY)
m = cv2.moments(thresh)
print(m)

x = int(m["m10"]/m["m00"])
y = int(m["m01"]/m["m00"])
cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

cv2.imshow("s", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
