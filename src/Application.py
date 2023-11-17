from util.Constant import *
from util.Variable import *
from util.Status import *
from util.SoundPlayer import *
from model.TrainData import *
from model.Detector import *
from model.Drawer import *
import cv2

STATUS = START


def isContinue():
    return not cv2.waitKey(1) & 0xFF == ESC


while isContinue():
    ret, frame = webcam.read()
    if ret is False:
        break

    shape_eyes = detectEyes(frame)
    drawEyes(frame, shape_eyes)

    if STATUS == START:
        play()
        STATUS = COLLECTING_OPEN_EYE_DATA
    elif STATUS == COLLECTING_OPEN_EYE_DATA:
        for shape_eye in shape_eyes:
            STATUS = getOpenEyeData(shape_eye)
            cv2.waitKey(1)
        if STATUS == COLLECTING_CLOSED_EYE_DATA:
            print("Press any key to collect closed eye data")
            cv2.waitKey(0)
            play()
    elif STATUS == COLLECTING_CLOSED_EYE_DATA:
        for shape_eye in shape_eyes:
            STATUS = getClosedEyeData(shape_eye)
            cv2.waitKey(1)
    elif STATUS == TRAINING_DATA:
        STATUS = trainData()
    elif STATUS == TRAINED_COMPLETE:
        if shape_eyes:
            isclosed = isClosed(shape_eyes)
            if isclosed:
                print(isclosed)
                drawText(frame, "CLOSED", (0, 30))
            else:
                print(isclosed)
                drawText(frame, "OPEN", (0, 30))
    else:
        print("waiting...")

    cv2.imshow("Driver Drowsiness Detection", frame)
webcam.release()
cv2.destroyAllWindows()