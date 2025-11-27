import cv2
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
cv2.waitKey(1000)
ret, frame2 = cap.read()
diff = cv2.absdiff(frame1, frame2)
cv2.imwrite("ex5.jpg", diff)
cap.release()
