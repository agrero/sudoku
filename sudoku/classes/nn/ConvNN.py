# as taken from the Pytorch documentation
import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvNN(nn.Module):
    def __init__(self, enc_sizes=[1, *[512 for i in range(15)]]):
        super().__init__()
        
        self.conv2d = nn.Sequential(*[self.conv_block(in_f, out_f)
                                      for in_f, out_f in zip(enc_sizes, enc_sizes[1:])])

        self.fc = nn.Sequential(self.linear(enc_sizes[-1] * 81, 1028))

        self.conv_out = nn.Sequential(
            nn.Conv2d(
                in_channels = enc_sizes[-1], # enc_sizes[-1] of incoming convolutions
                out_channels = 9, # probability outcome is 0-9 labels
                kernel_size=1, # generate predictions for each
            )
        ) # out dim = (batch, class probability, sudoku pos x, sudoku pos y)

    def linear(self, in_f, out_f):
        return nn.Sequential(
            nn.Linear(in_f, out_f),
            nn.ReLU(),
            nn.Dropout(p=0.2),
            nn.Linear(out_f, 81 * 9),
            nn.ReLU()
        )

    def conv_block(self, in_f, out_f):
        return nn.Sequential(
            nn.Conv2d(
                in_f, out_f, 
                kernel_size=3, 
                padding=1, 
                stride=1,
            ),
            nn.BatchNorm2d(out_f),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.conv2d(x.view(-1,9,9).unsqueeze(1))
        x = self.conv_out(x)
        
        x = torch.flatten(x, start_dim = 2)
        x = torch.permute(x, dims=(0, 2, 1))

        x = F.softmax(x, dim=2)
        return x.type(torch.float) 
