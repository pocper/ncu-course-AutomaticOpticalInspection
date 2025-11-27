import cv2
import numpy as np
img = cv2.imread('severalPatten.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 180, 250)
gray = cv2.medianBlur(gray, 3)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                           80, param1=250, param2=35, minRadius=20, maxRadius=100)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    txt = 'r:'+str(i[2])
    cv2.putText(img, txt, (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255, 255, 5), 2, cv2.LINE_AA)
cv2.imshow('detected circle', img)
cv2.waitKey()
