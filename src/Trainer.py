from util.Constant import *
from util.SoundPlayer import *
from util.Variable import *
from module.Detector import *
from module.Drawer import *
from module.Predictor import *
from trainer.Status import *
from trainer.TrainModel import *
from trainer.TrainDataCollector import *
import cv2

status = START
msg = ""
model = ""


def isContinue():
    return not cv2.waitKey(1) & 0xFF == ESC


while isContinue():
    ret, frame = webcam.read()
    if ret is False:
        break

    drawText(frame, "Trainer", (int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)) - 90, 20))
    shape_eyes = detectEyes(frame)
    drawEyes(frame, shape_eyes)

    if status == START:
        play()
        msg = "collecting open eye data..."
        status = COLLECTING_OPEN_EYE_DATA

    elif status == COLLECTING_OPEN_EYE_DATA:
        status = getOpenEyeData(shape_eyes)
        cv2.waitKey(1)
        if status == COLLECTING_CLOSED_EYE_DATA:
            print("Press Enter key to collect closed eye data")
            msg = "collecting closed eye data..."
            cv2.waitKey(0)
            play()

    elif status == COLLECTING_CLOSED_EYE_DATA:
        status = getClosedEyeData(shape_eyes)
        cv2.waitKey(1)

    elif status == TRAINING_DATA:
        model, accuracy, status = trainData()
        if status == TRAINED_COMPLETE:
            msg = f"train complete, accuracy = {accuracy:.1f}%"

    elif status == TRAINED_COMPLETE:
        (eye_status_msg, isclosed) = isClosed(model, shape_eyes)
        drawText(frame, f"EYE STATUS: {eye_status_msg}", (0, 50))

    drawText(frame, msg, (0, 20))
    cv2.imshow("Model Trainer", frame)
webcam.release()
cv2.destroyAllWindows()
