import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.EAR import eye_aspect_ratio
from trainer.Config import *
from trainer.Status import *
from util.SoundPlayer import play


def getOpenEyeData(shape_eye):
    global data_count

    if data_count < data_size - data_size/2:
        train_data[data_count] = eye_aspect_ratio(shape_eye)
        target_data[data_count] = 1
        data_count += 1
        if (data_count/(data_size/2)*100) % 10 == 0 :
            print(f"collecting {int(data_count/(data_size/2)*100)}% open eye data...")

    if data_count == data_size - data_size/2:
        print(f"Complete collect {int(data_size/2)} open eye datas")
        play()
        return COLLECTING_CLOSED_EYE_DATA

    return COLLECTING_OPEN_EYE_DATA


def getClosedEyeData(shape_eye):
    global data_count

    if data_count < data_size:
        train_data[data_count] = eye_aspect_ratio(shape_eye)
        target_data[data_count] = 0
        data_count += 1
        if ((data_count - data_size/2)/(data_size/2)*100) % 10 == 0 :
            print(f"collecting {int((data_count - data_size/2)/(data_size/2)*100)}% closed eye data...")

    if data_count == data_size:
        print(f"Complete collect {int(data_size/2)} closed eye datas")
        play()
        return TRAINING_DATA

    return COLLECTING_CLOSED_EYE_DATA
