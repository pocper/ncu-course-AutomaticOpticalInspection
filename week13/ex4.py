import numpy as np
import cv2


def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(thresh, 35, 125)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


W = 12
p = -1
d = 50
f = p*d/W
D = 0
cap = cv2.VideoCapture('cam_f_Calibration_d_Meas.mp4')

while True:
    ret, img = cap.read()
    cnt_max = findMarker(img)
    rect = cv2.minAreaRect(cnt_max)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    textf = "focal length="+str(np.round(f, 1))
    cv2.putText(img, textf, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2, cv2.LINE_AA)
    textD = "D-"+str(np.round(D, 1))
    cv2.putText(img, textD, (1000, 650), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("dfd", img)
    if(cv2.waitKey(10) & 0xff == ord('q')):
        break
    if(cv2.waitKey(10) & 0xff == ord('c')):
        p = rect[1][0]
        f = p*d/W
    p = rect[1][0]
    D = f*W/p
cv2.waitKey()
cap.release()
