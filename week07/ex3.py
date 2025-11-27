import cv2
img1 = cv2.imread('lena.jpg')
img2 = img1.copy()

img2[:21, :21] = img1[-21:, -21:]
img2[-21:, -21:] = img1[:21, :21]

cv2.imshow('image', img2)
cv2.waitKey()
