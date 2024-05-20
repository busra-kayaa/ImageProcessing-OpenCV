import cv2

img = cv2.imread("balon.jpg",0)
# img = cv2.imread("balon.jpg",cv2.IMREAD_GRAYSCALE); # resmi gri tonlamalı alır.
# print(img) # matris değerlerini verir

cv2.namedWindow("image",cv2.WINDOW_NORMAL) #resmin boyutu bu komut sayesinde değiştirilebilir.

cv2.imshow("image",img) ## pencere adı image olur

cv2.imwrite("copy.jpg",img) # kayıt eder.
cv2.waitKey(0) # bekleme, 500(milisaniye) yazarsak yarım saniye durur. 0 yazarsak bir tuşa basmadan kapanmaz.

cv2.destroyAllWindows() # açık olan bütün pencereleri kapatma komutu