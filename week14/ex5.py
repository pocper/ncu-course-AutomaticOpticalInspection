import numpy as np
import cv2
import random


def findCircle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                               300, param1=50, param2=30, minRadius=20, maxRadius=40)
    return circles[0]


def drawCircle(image, x, y, r):
    cv2.circle(image, (int(x), int(y)), int(r), (0, 0, 255), 2, cv2.LINE_AA)


def puttext(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)


def xy_axes(image, w, h):
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (0, 255, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (0, 255, 0), 2)
    cv2.circle(image, (int(w/2), int(h/2)), 10, (0, 255, 0), 2)


def drawCntMax(image, cntMax):
    rect = cv2.minAreaRect(cntMax)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    xc = int(rect[0][0])
    yc = int(rect[0][1])
    return (xc, yc)


f0 = 675
f1 = 593
l = 18  # cm

# =================================== #
img0 = cv2.imread('Position1(z69cm)_Cam0.jpg')
h0, w0, a0 = img0.shape

circle0 = findCircle(img0)
x0 = circle0[0][0]
y0 = circle0[0][1]
r0 = circle0[0][2]
Vx0 = np.arctan((x0-w0/2)/f0)*180/np.pi
Vy0 = np.arctan((y0-h0/2)/f0)*180/np.pi

drawCircle(img0, x0, y0, r0)

# =================================== #

img1 = cv2.imread('Position1(z69cm)_Cam1.jpg')
h1, w1, a1 = img1.shape

circle1 = findCircle(img1)
x1 = circle1[0][0]
y1 = circle1[0][1]
r1 = circle1[0][2]
Vx1 = np.arctan((x1-w1/2)/f1)*180/np.pi
Vy1 = np.arctan((y1-h1/2)/f1)*180/np.pi

drawCircle(img1, x1, y1, r1)

# =================================== #

a0 = np.arctan2((Vx0-w0/2), f0)
a1 = np.arctan2((Vx1-w1/2), f1)

b0 = np.arctan2((Vy0-h0/2), f0)
b1 = np.arctan2((Vy1-h1/2), f1)

z = l/(np.tan(a0)-np.tan(a1))
x = l/2*(np.tan(a0)+np.tan(a1))/(np.tan(a0)-np.tan(a1))
y0 = z*np.tan(b0)
y1 = z*np.tan(b1)


textPosition = f"({np.round(x, 1)},{np.round(y0, 1)},{np.round(z, 1)})"
puttext(img0, textPosition, 300, 140)
puttext(img1, textPosition, 300, 140)

xy_axes(img0, w0, h0)
xy_axes(img1, w1, h1)

cv2.imshow('c0', img0)
cv2.imshow('c1', img1)

cv2.waitKey()
cv2.destroyAllWindows()
