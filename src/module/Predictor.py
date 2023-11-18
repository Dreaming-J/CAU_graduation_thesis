import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.EAR import *
import numpy as np
import torch


def isClosed(model, shape_eyes):
    if not shape_eyes:
        return

    length = len(shape_eyes)
    test_data = np.zeros((length, 1))
    for i in range(length):
        test_data[i] = eye_aspect_ratio(shape_eyes[i])
    test_data = torch.tensor(test_data).to(torch.float32)

    prediction = model(test_data)

    return bool(prediction.mean() < 0.5)
