import cv2 as cv
import numpy as np
from skeletonize import *
from alg1 import *
from cleanLines import *

def genesis(frame):
    while True:
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        gausFrame = cv.GaussianBlur(grayFrame, (3, 3), 5)

        nayFrame = cv.Canny(gausFrame,18,130,2)

        lineys = cv.HoughLinesP(nayFrame, 1, np.pi / 180, 42,maxLineGap=5)
        xv = []
        yv = []
        xv2 = []
        yv2 = []
        lines = []

        if lineys is None:
            print("Hough Line Transform Failed! Skipping Frame...")
            break
        else:
            for line in lineys:
                x1, y1, x2, y2 = line[0]
                slope = findSlope(x1,y1,x2,y2)
                if -10 < slope and 10 > slope:
                    pass
                else:
                    #cv.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                    pass

                xv.append(x1)
                xv2.append(x2)
                yv.append(y1)
                yv2.append(y2)
                lines.append([[x1,y1],[x2,y2]])

        h, w, c = frame.shape

        leftLines, rightLines = leftRight(lines, w / 2)

        leftExtendedLines = []
        leftTopPoints = []
        leftBottomPoints = []

        for line in leftLines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]

            try:
                slope, inter = findLine(x1, y1, x2, y2)

                p1 = (int((0-inter)/slope), 0)
                p2 = (int((h - inter)/slope), h)

                #cv.line(frame, p1,p2,(0,255,0),3)

                leftExtendedLines.append([p1, p2])
                leftTopPoints.append(p1)
                leftBottomPoints.append(p2)


            except: pass

        rightExtendedLines = []
        rightTopPoints = []
        rightBottomPoints = []

        for line in rightLines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[1][0]
            y2 = line[1][1]

            try:
                slope, inter = findLine(x1, y1, x2, y2)


                if -20 >= int(slope) or int(slope) >= 1:

                    p1 = (int((0-inter)/slope), 0)
                    p2 = (int((h - inter)/slope), h)

                    #cv.line(frame, p1,p2,(0,0,255),3)

                    rightExtendedLines.append([p1, p2])
                    rightTopPoints.append(p1)
                    rightBottomPoints.append(p2)

            except: pass

        topLeftTotal = 0
        count = 0
        for i in leftTopPoints:
            topLeftTotal += i[0]
            count += 1
        try:
            topLeftTotal /= count

        except:
            print("No lines Detected! Passing Frame")
            break

        topLeftAv = (int(topLeftTotal), 0)

        bottomLeftTotal = 0
        count = 0
        for i in leftBottomPoints:
            bottomLeftTotal += i[0]
            count += 1

        bottomLeftTotal /= count

        bottomLeftAv = (int(bottomLeftTotal), h)

        topRightTotal = 0
        count = 0
        for i in rightTopPoints:
            topRightTotal += i[0]
            count += 1

        topRightTotal /= count

        topRightAv = (int(topRightTotal), 0)

        bottomRightTotal = 0
        count = 0
        for i in rightBottomPoints:
            bottomRightTotal += i[0]
            count += 1

        bottomRightTotal /= count

        bottomRightAv = (int(bottomRightTotal), h)

        cv.line(frame, topLeftAv, bottomLeftAv, (0,255,0),5)
        cv.line(frame, topRightAv, bottomRightAv, (255, 0, 0), 5)

        bottomCenterAv = (int((bottomRightTotal + bottomLeftTotal)/2), h)
        topCenterAv = (int((topRightTotal + topLeftTotal)/2), 0)

        cv.line(frame, topCenterAv, bottomCenterAv, (0,0,255),5)

        return [frame, nayFrame]
