"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import time

from cv2 import cv2
from gaze_tracking import GazeTracking
import keyboard


def startTracking():
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)

    start = time.time()
    prev = 0

    rpoints = 0
    lpoints = 0
    cpoints = 0
    totalruns = 0


    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        text = ""

        if gaze.is_blinking():
            print(prev)
            print("Blinking")
            text = "Blinking"
            prev = 1
        elif gaze.is_right():
            print(prev)
            print("Right")
            text = "Looking right"
            rpoints += 1
            prev = 2
        elif gaze.is_left():
            print(prev)
            print("Left")
            text = "Looking left"
            lpoints += 1
            prev = 3
        elif gaze.is_center():
            print(prev)
            print("Center")
            text = "Looking center"
            cpoints += 1
            prev = 4

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()

        totalruns += 1

        if((time.time() - start) > 20):
            break

        

    end = time.time()

    print("This is the total time elapsed: ", end - start)
    print("Points for looking at the right: ", rpoints)
    print("Points for looking at the left: ", lpoints)
    print("Points for looking at the center: ", cpoints)

    print("Total Runs: ", totalruns)