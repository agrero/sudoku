# as taken from the Pytorch documentation
import torch
import torch.nn as nn

class ConvNN(nn.Module):
    def __init__(self, n_features=9):
        super().__init__()
        
        self.conv2d = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=10,
                kernel_size=(3,3),
                padding=3
            ),
            nn.ReLU(),
            nn.MaxPool2d((2,2))
        )
        self.fc = nn.Sequential(
            nn.Linear(36, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 81 * n_features), # 81 tiles 9 possible outcomes including 0
            nn.ReLU()
        )

    def forward(self, x):
        x = self.conv2d(x)
        x = torch.flatten(x, 1) # flatten all except batch
        x = self.fc(x)  
        return x
    
"""
In PyTorch, convolutional layers are defined as torch.nn.Conv2d, 
there are 5 important arguments we need to know:

    in_channels: how many features are we passing in. 
    Our features are our colour bands, in greyscale, 
    we have 1 feature, in colour, we have 3 channels.

    out_channels: how many kernels do we want to use. 
    Analogous to the number of hidden nodes in a hidden 
    layer of a fully connected network.

    kernel_size: the size of the kernel. 
    Above we were using 3x3. 
    Common sizes are 3x3, 5x5, 7x7.

    stride: the “step-size” of the kernel.

    padding: the number of pixels we should pad to the 
    outside of the image so we can get edge pixels.

"""