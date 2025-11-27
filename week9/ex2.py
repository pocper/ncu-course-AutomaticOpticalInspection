import cv2
img = cv2.imread('lena.jpg')
rows, cols, deps = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
cv2.waitKey()
