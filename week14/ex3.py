import numpy as np
import cv2


def findMarker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 11)
    thresh = cv2.adaptiveThreshold(
        blur,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # cv2.imshow(str(random.randint(1, 99)), thresh)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


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


f0 = 867
f1 = 544
l = 10  # cm
img0 = cv2.imread('0609cam0.jpg')
h0, w0, a0 = img0.shape

img1 = cv2.imread('0609cam1.jpg')
h1, w1, a1 = img1.shape

cnt_max0 = findMarker(img0)
cnt_max1 = findMarker(img1)

(xc0, yc0) = drawCntMax(img0, cnt_max0)
(xc1, yc1) = drawCntMax(img1, cnt_max1)

a0 = np.arctan2((xc0-w0/2), f0)
a1 = np.arctan2((xc1-w1/2), f1)

b0 = np.arctan2((yc0-h0/2), f0)
b1 = np.arctan2((yc1-h1/2), f1)

z = l/(np.tan(a0)-np.tan(a1))
x = l/2*(np.tan(a0)+np.tan(a1))/(np.tan(a0)-np.tan(a1))
y0 = z*np.tan(b0)
y1 = z*np.tan(b1)

textf0 = "fL0="+str(f0)
puttext(img0, textf0, 450, 60)
textf1 = "fL1="+str(f1)
puttext(img1, textf1, 450, 60)
textx = "x="+str(np.round(x, 1))
puttext(img0, textx, 450, 100)
texty = "y="+str(np.round(y0, 1))
puttext(img0, texty, 450, 140)
textz = "z="+str(np.round(z, 1))
puttext(img0, textz, 450, 180)

xy_axes(img0, w0, h0)
xy_axes(img1, w1, h1)

cv2.imshow('c0', img0)
cv2.imshow('c1', img1)

cv2.waitKey()
cv2.destroyAllWindows()
