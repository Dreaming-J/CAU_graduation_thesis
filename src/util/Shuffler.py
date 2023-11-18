import numpy as np


def shuffle(x, y):
    idx = np.arange(x.shape[0])
    np.random.shuffle(idx)

    x = x[idx]
    y = y[idx]

    return x, y
