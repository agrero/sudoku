# as taken from the Pytorch documentation
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        
        # convolutional stack 
        self.conv(
            nn.Conv2d(3, 6, 5),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.MaxPool2d(2, 2)
        )   

        # fully connected (fc) stack
        self.fc(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10), # 10 classes out
            nn.ReLU()
        )

    def forward(self, x):
        x = self.conv(x)
        x = torch.flatten(x, 1) # flatten all except batch
        x = self.fc(x)  
        return x