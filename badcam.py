import cv2, numpy as np, pyvirtualcam

cam = cv2.VideoCapture(0)

BLUR = 7 #must be an odd number
FPS = 4

def main():
    _, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out = cv2.medianBlur(frame, BLUR)
    return out

if __name__ == "__main__":
    with pyvirtualcam.Camera(width=int(cam.get(3)), height=int(cam.get(4)), fps=FPS) as vcam:
        while True:
            frame = main()
            vcam.send(frame)
            vcam.sleep_until_next_frame()