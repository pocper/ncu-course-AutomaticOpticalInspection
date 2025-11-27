import cv2


def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(thresh, 35, 125)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


if __name__ == "__main__":
    cap = cv2.VideoCapture('motionPattens2.mov')
    while True:
        ret, frame = cap.read()
        if(ret == False):
            break

        CNT_MAX = findMarker(frame)
        cv2.drawContours(frame, [CNT_MAX], 0, (255, 0, 255), 2)
        cv2.imshow("dfd", frame)
        cv2.waitKey(100)
