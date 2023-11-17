import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.Status import *
from util.SoundPlayer import *
from util.Shuffler import *
import numpy as np
import torch
import torch.nn as nn
from scipy.spatial import distance as dist


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(1, 5),
            nn.Sigmoid(),
            nn.Linear(5, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        out_data = self.layer(x)
        return out_data


data_size = 100
train_data = np.zeros((data_size, 1))
target_data = np.zeros((data_size, 1))
data_count = 0
model = MyModel()


def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear * 100


def getOpenEyeData(shape_eye):
    global data_count

    if data_count < data_size - data_size/2:
        print("collecting {}th open eye data...".format(data_count + 1))
        train_data[data_count] = eye_aspect_ratio(shape_eye)
        target_data[data_count] = 1
        data_count += 1

    if data_count == data_size - data_size/2:
        print("Complete collect open eye data")
        play()
        return COLLECTING_CLOSED_EYE_DATA

    return COLLECTING_OPEN_EYE_DATA


def getClosedEyeData(shape_eye):
    global data_count

    if data_count < data_size:
        print("collecting {}th closed eye data...".format(data_count - int(data_size/2) + 1))
        train_data[data_count] = eye_aspect_ratio(shape_eye)
        target_data[data_count] = 0
        data_count += 1
    else:
        print("Complete collect closed eye data")
        play()
        return TRAINING_DATA

    return COLLECTING_CLOSED_EYE_DATA


def trainData():
    global train_data, target_data

    (train_data, target_data) = shuffle(train_data, target_data)
    X = torch.tensor(train_data).to(torch.float32)
    Y = torch.tensor(target_data).to(torch.float32)

    loss_func = nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.015)

    for epoch in range(2000):
        prediction = model(X)
        loss = loss_func(prediction, Y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    prediction = model(X)
    pred_final = (prediction > 0.5).float()
    accuracy = (pred_final == Y).float().mean()
    print('train complete, accuracy = {}%'.format(accuracy.item()*100))
    play()

    return TRAINED_COMPLETE


def isClosed(shape_eyes):
    length = len(shape_eyes)
    test_data = np.zeros((length, 1))
    for i in range(length):
        test_data[i] = eye_aspect_ratio(shape_eyes[i])
    test_data = torch.tensor(test_data).to(torch.float32)

    prediction = model(test_data)

    return prediction.mean() < 0.5
