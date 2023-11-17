import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.Constant import *
import cv2


def drawEyes(frame, shape_eyes):
    for shape_eye in shape_eyes:
        [cv2.circle(frame, (x, y), 1, RED, -1) for x, y in shape_eye]
        cv2.drawContours(frame, [cv2.convexHull(shape_eye)], -1, RED, 1)


def drawText(frame, text, position):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)
