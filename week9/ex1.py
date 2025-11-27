import numpy as np
import cv2
radius = 50
canvas = 300
image = np.zeros([canvas, canvas, 3], dtype='uint8')
red = cv2.circle(image, (canvas//2-radius//2, canvas //
                 2-radius), radius, (0, 0, 255), -1)
image = np.zeros([canvas, canvas, 3], dtype='uint8')
green = cv2.circle(image, (canvas//2+radius//2, canvas //
                   2-radius), radius, (0, 255, 0), -1)
image = np.zeros([canvas, canvas, 3], dtype='uint8')
blue = cv2.circle(image, (canvas//2, canvas//2), radius, (255, 0, 0), -1)
rb = cv2.addWeighted(red, 1, blue, 1, 0)
rgb = cv2.addWeighted(rb, 1, green, 1, 0)
cv2.imshow('rgb', rgb)
cv2.waitKey()
