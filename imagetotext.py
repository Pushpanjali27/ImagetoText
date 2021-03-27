import cv2
import numpy as np
import pytesseract as pytess
from PIL import Image
src_path = "D:\Python_Pro\p1.jpg"
pytess.pytesseract.tesseract_cmd = r"C:\Users\Pushpanjali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
img = cv2.imread(src_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
cv2.imwrite(src_path + "removed_noise.png", img)
cv2.imwrite(src_path + "thres.png", img)
result = pytess.image_to_string(Image.open(src_path + "thres.png"),lang="eng")
print (result)