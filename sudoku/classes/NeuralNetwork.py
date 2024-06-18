import torch 
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size=81) -> None:
        super().__init__(),
        self.input_size = input_size
        self.flatten = nn.Flatten()
        # need to convert data to float
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            nn.Linear(512,1024),
            nn.ReLU(),
            nn.Linear(1024,2048),
            nn.ReLU(),
            nn.Linear(2048,4096),
            nn.ReLU(),
            nn.Linear(4096,2048),
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, input_size * 9),
            nn.ReLU()
        )

    def forward(self, x):
        # might not have to flatten as its already linear
        x = self.flatten(x)
        x = x.to(torch.float32)
        logits = self.linear_relu_stack(x)
        
        # reshape for categorical
        # len(logits) = batch_size 
        logits = logits.reshape(len(logits), self.input_size, 9)

        logits = torch.softmax(logits, dim=2)

        return logits