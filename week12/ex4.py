import cv2
import numpy as np

img = cv2.imread('Coin and Paper.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 0, 100)
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)
N = lines.shape[0]

for n in range(N-1):
    r = lines[n, 0, 0]
    q = lines[n, 0, 1]
    L = 1000
    x0 = int(r*np.cos(q))
    y0 = int(r*np.sin(q))

    x1 = int(x0+L*np.sin(q))
    y1 = int(y0-L*np.cos(q))

    x2 = int(x0-L*np.sin(q))
    y2 = int(y0+L*np.cos(q))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow('img', img)
cv2.waitKey()
