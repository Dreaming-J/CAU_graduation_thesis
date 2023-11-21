import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.Shuffler import shuffle
from util.SoundPlayer import play
from trainer.Config import *
from trainer import Model
from trainer.Status import *
import torch
import torch.nn as nn


def save_model(model, train_data, target_data, pred_final, accuracy):
    torch.save(model.state_dict(), './model/detect_eye_blink_model.pth')
    f = open("./model/detect_eye_blink_model train result.txt", "w")
    f.write(f"모델 정확도: {accuracy.item()*100:.1f}\n\n")
    f.write("  좌우 EAR값  |  타겟  |  예측 |  정답  |\n")
    for i in range(len(train_data)):
        f.write(" {:05.2f} | {:05.2f} |    {}    |    {}    |  {:5s} |\n"
                .format(float(train_data[i][0]),
                        float(train_data[i][1]),
                        int(target_data[i]),
                        int(pred_final[i]),
                        str(bool(int(target_data[i]) == int(pred_final[i]))).rjust(5, ' ')))


def trainData():
    global train_data, target_data

    X = torch.tensor(train_data).to(torch.float32)
    Y = torch.tensor(target_data).to(torch.float32)

    model = Model.MyModel()
    loss_func = nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(3000):
        (X, Y) = shuffle(X, Y)

        prediction = model(X)
        loss = loss_func(prediction, Y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    prediction = model(X)
    pred_final = (prediction > 0.5).float()
    accuracy = (pred_final == Y).float().mean()
    print(f"train complete, accuracy = {accuracy.item()*100:.1f}%")
    save_model(model, train_data, target_data, pred_final, accuracy)
    play()

    return model, accuracy.item()*100, TRAINED_COMPLETE
