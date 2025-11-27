import cv2
import numpy as np

img = np.full((300, 300, 3), (255, 255, 255), np.uint8)

r = 100
center = [150, 150]
theta = np.linspace(0, 2*np.pi, 1000)
x = center[0]+r*np.cos(theta)
y = center[1]+r*np.sin(theta)
img[np.uint16(x), np.uint16(y), 1:] = 0
cv2.imshow("canvas", img)
cv2.waitKey()
