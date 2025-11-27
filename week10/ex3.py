import cv2
cap = cv2.VideoCapture(0)
sec = 10
for i in range(sec):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1000)

cap.release()
