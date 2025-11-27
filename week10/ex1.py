import cv2
import numpy as np
import random
img = cv2.imread('lena.jpg', 0)
shape = img.shape
numNoise = 2000
for i in range(numNoise):
    i = random.randint(0, shape[0]-1)
    j = random.randint(0, shape[1]-1)
    if(len(shape) == 2):
        img.itemset((i, j), 0)
    else:
        img.itemset((i, j, 0), 0)
        img.itemset((i, j, 1), 0)
        img.itemset((i, j, 2), 0)
dst = cv2.medianBlur(img, 5)
cv2.imshow('image', dst)
cv2.waitKey()
