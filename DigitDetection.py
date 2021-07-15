import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Reading image
img = cv2.imread('2.jpg')
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
#changing image to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((1,1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
#Code to detect Digits

hImg, wImg,_ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)
for b in boxes.splitlines():
     print(b)
     b = b.split(' ')
     print(b)
     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)