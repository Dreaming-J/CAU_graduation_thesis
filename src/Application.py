from module.Alarm import threadAlarm
from module.Detector import detectEyes
from module.Drawer import drawEyes
from module.Drawer import drawText
from module.Predictor import predictWithCompensator
from util.Constant import *
from util.SoundPlayer import play
from util.Variable import *
import cv2


def init():
    ret, frame = webcam.read()
    if ret is False:
        return
    play("car_open")
    print("Start Application!")
    cv2.imshow("Driver Drowsiness Detection", frame)


def isContinue():
    return not cv2.waitKey(1) & 0xFF == ESC


init()
while isContinue():
    ret, frame = webcam.read()
    if ret is False:
        break

    drawText(frame, "Application", (int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)) - 140, 20))
    shape_eyes = detectEyes(frame)
    drawEyes(frame, shape_eyes)

    (eye_status_msg, isclosed) = predictWithCompensator(model, shape_eyes, isclosed)
    drawText(frame, f"Eye Status: {eye_status_msg}", (0, 20))

    (alarm_status, elapsed_time) = threadAlarm(isclosed)
    drawText(frame, f"Elapsed Time: {elapsed_time:.1f}s", (0, 50))
    drawText(frame, f"Alarm Status: {alarm_status[0]}", (0, 80), alarm_status[1])

    cv2.imshow("Driver Drowsiness Detection", frame)
webcam.release()
cv2.destroyAllWindows()
