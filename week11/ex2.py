import numpy as np
import cv2
img = cv2.imread('img_dilate_google.png')
cv2.imshow('1', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, thr = cv2.threshold(gray, 200, 250, cv2.THRESH_BINARY_INV)
kernel = np.ones([3, 3])
dilated = cv2.dilate(thr, kernel, iterations=15)

contours, _ = cv2.findContours(
    dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 255, 0), 2)
cv2.imshow('2', img)
cv2.waitKey()
cv2.destroyAllWindows()
