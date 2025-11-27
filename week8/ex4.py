import cv2
import numpy as np

img = cv2.imread('lena.jpg')
cv2.rectangle(img, (20, 20), (80, 80), (255, 0, 0), 1)
cv2.circle(img, (50, 50), int(30*np.sqrt(2)), (255, 0, 0), 1)
cv2.imwrite('Lena_1.jpg', img)
