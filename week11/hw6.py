import numpy as np
import cv2
cap = cv2.VideoCapture('viewFromME_video1.mp4')

isFirstFrame = 0
while 1:
    ret, frame = cap.read()

    if(ret == False):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    a, thresh = cv2.threshold(gray, 150, 150, cv2.THRESH_BINARY_INV)

    if(isFirstFrame == 0):
        isFirstFrame = 1
    elif(isFirstFrame == 1):
        thresh_new = cv2.absdiff(thresh, thresh_last)
        kernel1 = np.ones([4, 4])
        dilated = cv2.dilate(thresh_new, kernel1, iterations=1)

        contours, _ = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            A = cv2.contourArea(c)
            if(A < 300):
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(100)

    thresh_last = thresh.copy()

cv2.waitKey()
cv2.destroyAllWindows()
