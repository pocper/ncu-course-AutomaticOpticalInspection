import cv2
import matplotlib.pyplot as plt
img = cv2.imread('coinOnDesk_lowC.jpg')
equ_b = cv2.equalizeHist(img[:, :, 0])
equ_g = cv2.equalizeHist(img[:, :, 1])
equ_r = cv2.equalizeHist(img[:, :, 2])
img_new = cv2.merge([equ_b, equ_g, equ_r])
histequ = cv2.calcHist([img_new], [0], None, [256], [0, 256])
cv2.imshow('new', img_new)
plt.bar(range(0, 256), histequ[:, 0])
plt.show()
