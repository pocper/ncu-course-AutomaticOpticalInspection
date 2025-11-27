import numpy as np
import cv2
img = cv2.imread('circles.jpg', 0)
kernel1 = np.ones((7, 7))
eroded = cv2.erode(img, kernel1, iterations=2)
kernel2 = np.ones((10, 10))
dilated = cv2.dilate(eroded, kernel2, iterations=2)
cv2.imshow('o', img)
cv2.imshow('df', dilated)
cv2.waitKey()
