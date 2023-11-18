import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.EAR import eye_aspect_ratio
import numpy as np
import torch


def isClosed(model, shape_eyes):
    if not shape_eyes:
        return "NOT DETECTED", None

    length = len(shape_eyes)
    test_data = np.zeros((length, 1))
    for i in range(length):
        test_data[i] = eye_aspect_ratio(shape_eyes[i])
    test_data = torch.tensor(test_data).to(torch.float32)

    prediction = model(test_data)
    prediction = bool(prediction.mean() < 0.5)

    if prediction:
        return "CLOSED", prediction

    return "OPEN", prediction


def predictWithCompensator(model, shape_eyes, current=None):
    previous = current
    (eye_status_msg, current) = isClosed(model, shape_eyes)

    if current is None:
        return eye_status_msg, previous
    return eye_status_msg, current
