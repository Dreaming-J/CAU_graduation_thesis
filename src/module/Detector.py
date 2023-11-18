import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.Constant import idx_eyes
from util.Variable import detector
from util.Variable import predictor
import cv2
from imutils import face_utils


def detectEyes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)

    shape_eyes = []

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        [shape_eyes.append(shape[start:end]) for (start, end) in idx_eyes]

    return shape_eyes
