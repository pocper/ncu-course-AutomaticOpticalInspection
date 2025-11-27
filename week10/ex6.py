import numpy as np
import cv2
frame1 = cv2.imread("frame1.jpg")
frame2 = cv2.imread("frame2.jpg")
diff = cv2.absdiff(frame1, frame2)
gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
a, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
b = np.where(thresh == 255)
X = int(np.average(b[1]))
Y = int(np.average(b[0]))
cv2.circle(frame1, (X, Y), 20, (255, 0, 0), 5)
cv2.imwrite("ex6_1.jpg", thresh)
cv2.imwrite("ex6_2.jpg", frame1)
