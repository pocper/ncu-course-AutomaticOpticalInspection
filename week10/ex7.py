import numpy as np
import cv2
cap = cv2.VideoCapture(0)
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while(1):
    key = cv2.waitKey(100) & 0xff
    if(key == ord('q')):
        break

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    b = np.where(thresh == 255)
    Y = np.average(b[0])
    X = np.average(b[1])
    if(not np.isnan(X) and not np.isnan(Y)):
        X = int(X)
        Y = int(Y)
        cv2.circle(frame1, (X, Y), 20, (255, 0, 0), 5)
        cv2.imshow("dfy", frame1)
        frame1 = frame2.copy()
        cv2.waitKey(50)
    ret2, frame2 = cap.read()
cap.release()
