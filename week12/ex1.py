import cv2
img = cv2.imread('0518_5p.png')
ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(th, 127, 255)
cv2.imshow('eg', edges)
cv2.waitKey()
