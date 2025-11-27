import random
import numpy as np
import cv2
img = cv2.imread('img_dilate_google.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, thr = cv2.threshold(gray, 200, 250, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x+w, y+h), (random.randint(0, 255),
                  random.randint(0, 255), random.randint(0, 255)), 2)
    cv2.imshow('img', img)
    cv2.waitKey(500)
cv2.waitKey()
cv2.destroyAllWindows()
