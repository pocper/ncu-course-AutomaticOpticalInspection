import cv2
import numpy as np
img = cv2.imread('IMG_3973.JPG')
img_resize = cv2.resize(img, (960, 540))
gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200,
                        minLineLength=100, maxLineGap=10)


for n in range(len(lines)):
    x1 = lines[n, 0, 0]
    y1 = lines[n, 0, 1]
    x2 = lines[n, 0, 2]
    y2 = lines[n, 0, 3]
    cv2.line(img_resize, (x1, y1), (x2, y2), (0, 0, 255), 5)


def length(vec):
    return (vec[0]**2+vec[1]**2)**0.5


a = (-(lines[0, 0, 2]-lines[0, 0, 0]), -(lines[0, 0, 3]-lines[0, 0, 1]))
b = (lines[1, 0, 2]-lines[1, 0, 0], lines[1, 0, 3]-lines[1, 0, 1])
theta = np.arccos(np.dot(a, b)/(length(a)*length(b)))*180/np.pi
print(f'theta = {theta} [deg]')

cv2.imshow('img', img_resize)
cv2.waitKey()
