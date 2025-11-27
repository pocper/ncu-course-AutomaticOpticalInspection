import numpy as np
import cv2
img = cv2.imread('test.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def mask(hsv, lower, upper):
    return cv2.inRange(hsv, np.asarray(lower), np.asarray(upper))


def count_area(mask):
    area = 0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if(mask[i][j] > 0):
                area += 1
    return area


mask_red = mask(hsv, [0, 43, 46], [10, 255, 255])
mask_green = mask(hsv, [35, 43, 46], [77, 255, 255])
mask_blue = mask(hsv, [100, 43, 46], [124, 255, 255])

print(f'area of R = {count_area(mask_red)}')
print(f'area of G = {count_area(mask_green)}')
print(f'area of B = {count_area(mask_blue)}')
