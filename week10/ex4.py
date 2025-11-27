import cv2
import numpy as np

img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('messi5p.jpg')
diff = cv2.absdiff(img1, img2)
cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.imshow('s', diff)
cv2.waitKey()
