from util.Constant import *
from util.Variable import *
from module.Detector import *
from module.Drawer import *
from module.Predictor import *
from trainer import Model
import cv2
import torch

model = Model.MyModel()
model.load_state_dict(torch.load("./model/detect_eye_blink_model.pth"))
model.eval()


def isContinue():
    return not cv2.waitKey(1) & 0xFF == ESC


while isContinue():
    ret, frame = webcam.read()
    if ret is False:
        break

    drawText(frame, "Application", (int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)) - 140, 20))
    shape_eyes = detectEyes(frame)
    drawEyes(frame, shape_eyes)

    isclosed = isClosed(model, shape_eyes)
    if isclosed is True:
        eye_status = "CLOSED"
    elif isclosed is False:
        eye_status = "OPEN"
    else:
        eye_status = ""
    drawText(frame, "EYE STATUS: {}".format(eye_status), (0, 20))

    cv2.imshow("Driver Drowsiness Detection", frame)
webcam.release()
cv2.destroyAllWindows()
