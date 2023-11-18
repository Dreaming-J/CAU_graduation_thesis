from module.Alarm import alarm
from module.Detector import detectEyes
from module.Drawer import drawEyes
from module.Drawer import drawText
from module.Predictor import predictWithCompensator
from util.Constant import *
from util.SoundPlayer import play
from util.Variable import *
import cv2
import time
import threading


def isContinue():
    return not cv2.waitKey(1) & 0xFF == ESC


play("car_open")
print("Start Application!")
while isContinue():
    ret, frame = webcam.read()
    if ret is False:
        break

    drawText(frame, "Application", (int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)) - 140, 20))
    shape_eyes = detectEyes(frame)
    drawEyes(frame, shape_eyes)

    (eye_status_msg, isclosed) = predictWithCompensator(model, shape_eyes, isclosed)
    drawText(frame, f"EYE STATUS: {eye_status_msg}", (0, 20))

    if isclosed is False:
        start_closed_eye = time.time()
        elapsed_time = 0
    elif isclosed is True:
        elapsed_time = time.time() - start_closed_eye
        thread = threading.Thread(target=alarm, args=(elapsed_time,))
        thread.start()
    drawText(frame, f"Elapsed Time: {elapsed_time:.1f}s", (0, 50))

    cv2.imshow("Driver Drowsiness Detection", frame)
webcam.release()
cv2.destroyAllWindows()
