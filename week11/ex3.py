import numpy as np
import cv2
cap = cv2.VideoCapture('IMG_3006.MOV')

while 1:
    ret, frame = cap.read()
    if(ret == True):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        a, thr = cv2.threshold(gray, 100, 100, cv2.THRESH_BINARY_INV)
        kernel1 = np.ones([13, 13])
        eroded = cv2.erode(thr, kernel1, iterations=1)
        kernel2 = np.ones([23, 23])
        dilated = cv2.dilate(eroded, kernel2, iterations=3)

        contours, _ = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            x = int((max(c[:, 0, 0])+min(c[:, 0, 0]))/2)
            y = int((max(c[:, 0, 1])+min(c[:, 0, 1]))/2)
            cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)
        cv2.drawContours(frame, contours, -1, (255, 255, 0), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(100)
    else:
        break

cv2.waitKey()
cv2.destroyAllWindows()
