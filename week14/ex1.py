import numpy as np
import cv2
W = 12
p = -1.0
d = 50
f = p*d/W
D = 0
cap = cv2.VideoCapture('motionPattens3.mov')
ret, img = cap.read()
h, w, a = img.shape


def findMarker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


def xy_axes(image, w, h):
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (0, 255, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (0, 255, 0), 2)
    cv2.circle(image, (int(w/2), int(h/2)), 10, (0, 255, 0), 2)


def puttext(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)


def p2center(image, xc, yc, w, h):
    cv2.circle(image, (xc, yc), 7, (0, 0, 255), -1)
    cv2.line(image, (int(w/2), int(h/2)), (xc, yc), (0, 0, 255), 2)
    cv2.line(image, (xc, yc), (int(w/2), yc), (0, 0, 255), 2)
    cv2.line(image, (xc, yc), (xc, int(h/2)), (0, 0, 255), 2)


while ret:
    xy_axes(img, w, h)
    cnt_max = findMarker(img)
    rect = cv2.minAreaRect(cnt_max)
    xc = int(rect[0][0])
    yc = int(rect[0][1])
    Vx = np.arctan((xc-w/2)/f)*180/np.pi
    Vy = np.arctan((yc-h/2)/f)*180/np.pi
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    textf = 'fL='+str(np.round(f, 1))
    puttext(img, textf, 700, 80)
    textD = 'D='+str(np.round(D, 1))
    puttext(img, textD, 700, 120)
    textVx = 'Vx='+str(np.round(Vx, 1))
    puttext(img, textVx, 700, 160)
    textVy = 'Vy='+str(np.round(Vy, 1))
    puttext(img, textVy, 700, 200)
    p2center(img, xc, yc, w, h)
    cv2.imshow('dfd', img)
    if(cv2.waitKey(10) & 0xff == ord('q')):
        break
    if(cv2.waitKey(10) & 0xff == ord('c')):
        p = rect[1][0]
        f = p*d/W
    p = rect[1][0]
    D = f*W/p
    ret, img = cap.read()
cap.release()
cv2.destroyAllWindows()
