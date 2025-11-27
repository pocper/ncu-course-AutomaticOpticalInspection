import numpy as np
import cv2


def findMarker(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours) > 0):
        cnt_max = max(contours, key=cv2.contourArea)
        return cnt_max
    return []


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
L_orange = np.array([41, 133, 231])
U_orange = np.array([153, 217, 255])


cap0 = cv2.VideoCapture('videoCam0_calbrateNballPos.mp4')
cap1 = cv2.VideoCapture('videoCam1_calbrateNballPos.mp4')

while True:
    # =================================== #

    ret0, img0 = cap0.read()
    if(ret0 == False):
        break
    h0, w0, a0 = img0.shape
    mask0 = cv2.inRange(img0, L_orange, U_orange)
    cnt_max0 = findMarker(mask0)
    if(len(cnt_max0) == 0):
        continue
    x, y = drawCntMax(img0, cnt_max0)
    rect0 = cv2.minAreaRect(cnt_max0)
    x0 = int(rect0[0][0])
    y0 = int(rect0[0][1])
    Vx0 = np.arctan((x0-w0/2)/f0)*180/np.pi
    Vy0 = np.arctan((y0-h0/2)/f0)*180/np.pi
    box = np.int0(cv2.boxPoints(rect0))
    cv2.drawContours(img0, [box], 0, (0, 0, 255), 2)

    # =================================== #

    ret1, img1 = cap1.read()
    if(ret1 == False):
        break
    h1, w1, a1 = img1.shape
    mask1 = cv2.inRange(img1, L_orange, U_orange)
    cnt_max1 = findMarker(mask1)
    if(len(cnt_max1) == 0):
        continue
    x, y = drawCntMax(img1, cnt_max1)
    rect1 = cv2.minAreaRect(cnt_max1)
    x1 = int(rect1[0][0])
    y1 = int(rect1[0][1])
    Vx1 = np.arctan((x1-w1/2)/f1)*180/np.pi
    Vy1 = np.arctan((y1-h1/2)/f1)*180/np.pi
    box = np.int0(cv2.boxPoints(rect1))
    cv2.drawContours(img1, [box], 0, (0, 0, 255), 2)

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
    puttext(img0, textPosition, 30, 50)
    puttext(img1, textPosition, 30, 50)

    xy_axes(img0, w0, h0)
    xy_axes(img1, w1, h1)

    cv2.imshow('c0', img0)
    cv2.imshow('c1', img1)

    if(cv2.waitKey(5) & 0xff == ord('q')):
        break
cap0.release()
cap1.release()
cv2.destroyAllWindows()
