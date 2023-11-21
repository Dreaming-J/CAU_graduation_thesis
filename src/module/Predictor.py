import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.EAR import getEAR
import torch


def isClosed(model, shape_eyes):
    if not shape_eyes:
        return "NOT DETECTED", None

    test_data = torch.tensor(getEAR(shape_eyes)).to(torch.float32)

    prediction = model(test_data)
    prediction = bool(prediction.mean() < 0.5)

    if prediction:
        return "CLOSED", prediction

    return "OPEN", prediction


def predictWithCompensator(model, shape_eyes, previous=None):
    (eye_status_msg, current) = isClosed(model, shape_eyes)

    if current is None:
        return eye_status_msg, previous
    return eye_status_msg, current
