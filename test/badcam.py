import cv2, numpy as np
from time import sleep
from random import randint

cam = cv2.VideoCapture(0)

BLUR = 7 # must be an odd number
FPS = 4

def main():
    _, frame = cam.read()
    out = cv2.medianBlur(frame, BLUR)
    return out

if __name__ == "__main__":
    while True:
        frame = main()
        cv2.imshow("", frame)
        # sleep(1 / randint(2, 10))
        sleep(1 / FPS)
        if cv2.waitKey(1) & 0xff == ord('q'):
            exit()