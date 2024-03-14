import cv2
import numpy as np

def perspectiveTransform(frame,p1,p2,p3,p4):
    pts1 = np.float32([p1, p2, p3, p4])
    pts2 = np.float32([[0, 640], [0, 0], [400, 0], [400, 650]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    procFrame = cv2.warpPerspective(frame, matrix, (500, 600))

    return procFrame
