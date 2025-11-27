import numpy as np
import cv2
# global variable
canvas = 300
compansation = 10
rec1_length = 150
circle_radius = rec1_length//2
ellipse_long_axis = rec1_length//2-compansation
ellipse_short_axis = 30

# canvas setting
img = np.zeros([canvas, canvas, 3], dtype='uint8')

# draw corner rectangle
# left-upper corner
cv2.rectangle(img, (0, 0), (canvas//2, canvas//2), (0, 0, 255), -1)
# right-upper corner
cv2.rectangle(img, (canvas//2, 0), (canvas, canvas//2), (0, 255, 0), -1)
# left-lower corner
cv2.rectangle(img, (0, canvas//2), (canvas//2, canvas), (255, 0, 0), -1)
# right-lower corner
cv2.rectangle(img, (canvas//2, canvas//2),
              (canvas, canvas), (255, 255, 255), -1)

# draw circle
cv2.circle(img, (canvas//2, canvas//2), circle_radius, (255, 255, 0), -1)

# draw first rectangle
cv2.rectangle(img, (canvas//2-rec1_length//2, canvas//2-rec1_length//2),
              (canvas//2+rec1_length//2, canvas//2+rec1_length//2), (0, 0, 0), 5)

# draw second rectangle
img1 = np.zeros([canvas, canvas, 3], dtype='uint8')
rec1 = cv2.rectangle(img1, ((int)(canvas//2-rec1_length//(2*np.sqrt(2))+1), (int)(canvas//2-rec1_length//(2*np.sqrt(2))+1)),
                     ((int)(canvas//2+rec1_length//(2*np.sqrt(2))-1), (int)(canvas//2+rec1_length//(2*np.sqrt(2))-1)), (0, 255, 255), 3)
M = cv2.getRotationMatrix2D((canvas//2, canvas//2), 45, 1)
rec1 = cv2.warpAffine(rec1, M, (canvas, canvas))
img = cv2.addWeighted(rec1, 1, img, 1, 0)

# draw ellipse
cv2.ellipse(img, (canvas//2, canvas//2),
            (ellipse_long_axis, ellipse_short_axis//2), 360, 0, 360,  (127, 127, 127), 5)

# save image
cv2.imwrite('img0419.jpg', img)

# draw image
cv2.imshow('test', img)
cv2.waitKey()
