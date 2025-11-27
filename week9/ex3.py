import cv2
import numpy as np
img = cv2.imread('coinOnDesk.jpg',0)
Y, X = img.shape
cv2.circle(img, (X, Y), 20, (0, 0, 255), -1)
cv2.circle(img, (105, 125), 5, (0, 0, 255), 2)
cv2.circle(img, (105, 125), 5, (0, 0, 255), 2)
cv2.circle(img, (433, 125), 5, (0, 0, 255), 2)
cv2.circle(img, (35, 305), 5, (0, 0, 255), 2)
cv2.circle(img, (535, 305), 5, (0, 0, 255), 2)

s = np.array([[105, 125], [433, 125], [35, 305], [535, 305]], np.float32)
d = np.array([[135, 35], [435, 35], [135, 305], [435, 305]], np.float32)
p = cv2.getPerspectiveTransform(s, d)
r = cv2.warpPerspective(img, p, (X, Y))
cv2.imshow('img', img)
cv2.imshow('r', r)
cv2.waitKey()
