from cv2 import circle
import numpy as np
import cv2
l = 30  # cm
f = 1000  # pixel
u0 = 0  # degree
u1 = 0  # degree

cap1 = cv2.VideoCapture('0609_circleCam0.jpg')
cap2 = cv2.VideoCapture('0609_circleCam1.jpg')
ret1, img1 = cap1.read()
h1, w1, a1 = img1.shape

ret2, img2 = cap2.read()
h2, w2, a2 = img2.shape


def findCircle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                               100, param1=250, param2=20, minRadius=0, maxRadius=200)
    return circles[0]


def xy_axes(image, w, h):
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (0, 255, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (0, 255, 0), 2)
    cv2.circle(image, (int(w/2), int(h/2)), 10, (0, 255, 0), 2)


def puttext(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)


def p2center(image, xc, yc, w, h):
    cv2.circle(image, (xc, yc), 1, (0, 0, 255), -1)
    cv2.line(image, (int(w/2), int(h/2)), (xc, yc), (0, 0, 255), 2)
    cv2.line(image, (xc, yc), (int(w/2), yc), (0, 0, 255), 2)
    cv2.line(image, (xc, yc), (xc, int(h/2)), (0, 0, 255), 2)


# =================================== #

circle1 = findCircle(img1)
x1 = circle1[0][0]
y1 = circle1[0][1]
r1 = circle1[0][2]

Vx1 = np.arctan((x1-w1/2)/f)*180/np.pi
Vy1 = np.arctan((y1-h1/2)/f)*180/np.pi

xy_axes(img1, w1, h1)
textVx = 'Vx='+str(np.round(Vx1, 1))
puttext(img1, textVx, 500, 140)
textVy = 'Vy='+str(np.round(Vy1, 1))
puttext(img1, textVy, 500, 180)
p2center(img1, int(x1), int(y1), w1, h1)

# =================================== #

circle2 = findCircle(img2)
x2 = circle2[0][0]
y2 = circle2[0][1]
r2 = circle2[0][2]

Vx2 = np.arctan((x2-w2/2)/f)*180/np.pi
Vy2 = np.arctan((y2-h2/2)/f)*180/np.pi

xy_axes(img2, w2, h2)
textVx = 'Vx='+str(np.round(Vx2, 1))
puttext(img2, textVx, 500, 140)
textVy = 'Vy='+str(np.round(Vy2, 1))
puttext(img2, textVy, 500, 180)
p2center(img2, int(x2), int(y2), w2, h1)

# =================================== #

d = l/(np.tan(Vx1*np.pi/180)-np.tan(Vx2*np.pi/180))
textD = 'D='+str(np.round(d, 1))
puttext(img1, textD, 500, 220)
puttext(img2, textD, 500, 220)
cv2.imshow('1', img1)
cv2.imshow('2', img2)

cv2.waitKey()
cap1.release()
cap2.release()
cv2.destroyAllWindows()
