import cv2
img = cv2.imread('A4paper70cm.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)

edged = cv2.Canny(thresh, 35, 125)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_NONE)

imax = 0
areamax = 0
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if(area > areamax):
        areamax = area
        imax = i
cv2.drawContours(img, contours[imax], -1, (255, 0, 255), 2)
cv2.imshow("dfd", img)
cv2.waitKey()
