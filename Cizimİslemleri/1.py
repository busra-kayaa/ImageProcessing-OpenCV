import cv2
import numpy as np  # matematiksel işlemler için kullanılmış kutuphane

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 200  # zerostan 0 gelir
# +120 pencerede gri oluyor
# +200 pencerede acik gri oluyor
# +255 pencerede beyaz oluyor, 3-> renkli demek
# 8 bitlik pozitif tam sayıları tutan numpay dizisi
print(canvas)  # 3x3lük matrisler
cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

