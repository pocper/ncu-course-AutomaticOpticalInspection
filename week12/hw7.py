import cv2
import numpy as np
cap = cv2.VideoCapture('2coins_motion.wmv')
# cap = cv2.VideoCapture('video.mp4')


def factorial(n):
    sum = 1
    while(n > 0):
        sum *= n
        n -= 1
    return sum


def combination(n, m):
    return (int)(factorial(n)/(factorial(n-m)*factorial(m)))


while True:
    ret, frame = cap.read()
    if(ret == False):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                               100, param1=250, param2=50, minRadius=10, maxRadius=200)
    circles = np.int16(np.around(circles))
    c = circles[0]
    N = len(c)
    for i in range(N):
        x = c[i, 0]
        y = c[i, 1]
        r = c[i, 2]
        cv2.circle(frame, (x, y), r, (0, 0, 255), 2)

    # 2 coin 1 line => C(2,2)
    # 3 coin 3 line => C(3,2)
    for i in range(combination(N, 2)):
        if(i != combination(N, 2)-1 or N == 2):
            a = i
            b = i+1
        else:
            a = i
            b = 0
        x0 = c[a, 0]
        y0 = c[a, 1]

        x1 = c[b, 0]
        y1 = c[b, 1]
        cv2.line(frame, (x0, y0), (x1, y1), (0, 0, 255), 2)
        xm = (x0+x1)//2
        ym = (y0+y1)//2
        txt = f'D{i}'
        cv2.putText(frame, txt, (xm, ym), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 0, 0), 2, cv2.LINE_AA)
        distance = np.sqrt((x1-x0)**2+(y1-y0)**2)
        txt = f'D{i}={str(np.round(distance, 1))}'
        cv2.putText(frame, txt, (10, 30*(i+1)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('detected circle', frame)
    cv2.waitKey(100)
