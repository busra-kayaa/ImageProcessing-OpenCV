# pytesseract ile Resimden Yazı Okuma
from PIL import Image
import pytesseract

img = Image.open("merhabaDunya.png")
text = pytesseract.image_to_string(img, lang="eng")

print(text)