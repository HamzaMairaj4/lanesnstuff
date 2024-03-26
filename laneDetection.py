import cv2 as cv
import numpy as np
from skeletonize import *

def genesis(frame):
    while True:
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # cv.imshow('frame', grayFrame)
        # cv.waitKey(0)

        gausFrame = cv.GaussianBlur(grayFrame, (3, 3), 5)
        # cv.imshow('frame', gausFrame)
        # cv.waitKey(0)

        nayFrame = cv.Canny(gausFrame,55,20)
        # cv.imshow('frame',nayFrame)
        # cv.waitKey(0)

        nayFrame = spookyScary(nayFrame)

        lineys = cv.HoughLinesP(nayFrame, 1, np.pi / 90, 81,maxLineGap=5)
        # xv = []
        # yv = []
        # xv2 = []
        # yv2 = []

        if lineys is None:
            print("Hough Line Transform Failed! Skipping Frame...")
            break
        else:
            for line in lineys:
                x1, y1, x2, y2 = line[0]
                cv.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
                # xv.append(x1+5)
                # xv2.append(x2+5)
                # yv.append(y1+5)
                # yv2.append(y2+5)

        return frame, nayFrame
