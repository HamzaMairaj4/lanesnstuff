from videoStream import *
from skeletonize import *
from perspectiveTransform import *
from laneDetection import *
import cv2 as cv
import numpy as np

videoStreamProcess('My+Movie.mov')

# #bottom left
# p1 = [840, 1350]
# # top left
# p2 = [1600, 900]
# # top right
# p3 = [2100, 900]
# # bottom right
# p4 = [2540, 1350]
#
# hullo = cv.imread('OHYEAH.png')
# procFrame = perspectiveTransform(hullo,p1, p2, p3, p4)
#
# cv.imshow('transfromers',procFrame)
#
# nallo, gallo = genesis(procFrame)
#
# procFrame = cv.cvtColor(procFrame, cv.COLOR_BGR2GRAY)
#
#
#
#
#
#
#
# pts = np.array([p1, p2, p3, p4],
#                np.int32)
#
# pts = pts.reshape((-1, 1, 2))
#
# isClosed = True
#
# # Blue color in BGR
# color = (255, 0, 0)
#
# # Line thickness of 2 px
# thickness = 2
#
# # Using cv2.polylines() method
# # Draw a Blue polygon with
# # thickness of 1 px
# image = cv2.polylines(hullo, [pts],
#                       isClosed, color, thickness)
#
#
# cv.imshow('ajadkfjhlsa',nallo)
# cv.imshow('jahdfgl',gallo)
#
# cv.waitKey(0)