import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(1, 15),
            nn.Sigmoid(),
            nn.Linear(15, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        out_data = self.layer(x)
        return out_data
