import numpy as np


def shuffle(x, y):
    idx = np.arange(x.shape[0])
    np.random.shuffle(idx)

    X = x[idx]
    Y = y[idx]

    return X, Y
