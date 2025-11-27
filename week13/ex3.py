import cv2
import numpy as np


def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(thresh, 35, 125)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


if __name__ == "__main__":
    cap = cv2.VideoCapture('motionPattens3.mov')
    while True:
        ret, frame = cap.read()
        if(ret == False):
            break

        CNT_MAX = findMarker(frame)
        rect = cv2.minAreaRect(CNT_MAX)
        box = np.int0(cv2.boxPoints(rect))
        cv2.drawContours(frame, [box], 0, (255, 0, 255), 2)
        txt = 'width = '+str(round(rect[1][0], 1))
        cv2.putText(frame, txt, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("dfd", frame)
        cv2.waitKey(100)
