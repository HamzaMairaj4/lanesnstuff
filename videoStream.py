import cv2 as cv
import numpy as np
from perspectiveTransform import *
from laneDetection import *

def videoStreamProcess(port):
    # open video
    capture = cv.VideoCapture(port)


    while True:
        # capture frame
        ret, frame = capture.read()

        # establish trapezoid mask

        # if frame isn't read correctly, kill process
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # extract mask from frame
        rectFrame = frame #[upperLeft[1]: bottomRight[1], upperLeft[0]:bottomRight[0]]

        # process frame
        procFrame = rectFrame
        #try:
            # if canny detects lines
            # procFrame, nayFrame = curveCenter(rectFrame)
        #except:
            # if canny doesnt detect lines
            # procFrame=curveCenter(rectFrame)

        #bottom left
        p1 = [420, 700]
        #top left
        p2 = [725, 500]
        #top right
        p3 = [1025, 500]
        #bottom right
        p4 = [1320, 700]

        # replace mask
        try:
            procFrame = perspectiveTransform(frame,p1, p2, p3, p4)


        except:
            print("Failed")
            pass

        pts = np.array([p1, p2,p3,p4],
                       np.int32)

        pts = pts.reshape((-1, 1, 2))

        isClosed = True

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        # Using cv2.polylines() method
        # Draw a Blue polygon with
        # thickness of 1 px
        image = cv2.polylines(frame, [pts],
                              isClosed, color, thickness)

        showFrame = genesis(procFrame)

        # Display the resulting frame
        cv.imshow('frame', frame)
        try:
            cv.imshow('show',showFrame)

        except:
            print("NYEEEEOW")
            pass
        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()




