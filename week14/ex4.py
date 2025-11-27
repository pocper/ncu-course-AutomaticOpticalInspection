import cv2
import numpy as np


def findMarker(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


def drawCntMax(image, cntMax):
    rect = cv2.minAreaRect(cntMax)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    xc = int(rect[0][0])
    yc = int(rect[0][1])
    return (xc, yc)


def puttext(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)


def points(event, x, y, flags, param):
    global x_init, y_init, img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        x_init, y_init = x, y
        print('(x,y)=', (x, y), "(B,G,R)=", img[int(y), int(x), :])


# cv2.namedWindow('img')
# img = cv2.imread('traffic0609_2.jpg')
# cv2.setMouseCallback('img', points)
# cv2.imshow('img', img)

img = cv2.imread('traffic0609_2.jpg')
L_blue = np.array([57, 22, 12])
U_blue = np.array([158, 74, 18])
mask = cv2.inRange(img, L_blue, U_blue)
cnt = findMarker(mask)
x, y = drawCntMax(img, cnt)
textX = 'X='+str(x)
textY = 'Y='+str(y)
puttext(img, textX, 900, 100)
puttext(img, textY, 900, 140)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
