from sudoku.classes.ConvNN import ConvNN
from sklearn.metrics import confusion_matrix
from sudoku.classes.Board import Board

import numpy as np

import torch


# this should generate a confusion matrix of predicted vs actual labels
# # this should use the forward function
# # 
class Evaluator():
    def __init__(self):
        pass

    @torch.no_grad()
    def confusion_matrix(self, dataloader, model, device='cuda'):
        """Generate a Confusion Matrix for all the data available in a 
        pytorch Dataloader class

        # WE SHOULD MAKE THIS MORE LIKE BELOW
        
        returns -> np.darray containing the confusion matrix for sudoku classfication error"""
        # instantiate to be added to
        conf_matrix = np.zeros((9,9))
        
        for batch, (X, y) in enumerate(dataloader):
            print(f'Progress: [{batch * dataloader.batch_size}/{len(dataloader.dataset)}]')
            X, y = X.to(device), y            
            
            # flatten preds/labels for confusion_matrix
            pred = torch.flatten(
                torch.argmax(
                    model(X).cpu(),
                    dim = 2 
                )
            ).detach().numpy() 
            y = torch.flatten(
                torch.argmax(y, dim=2)
            ) 
            conf_matrix += confusion_matrix(
                y_true=y,
                y_pred=pred
            )
            
            # if batch >= 10:
            #     break
        return conf_matrix

    def board_check(self, X, y):
        """
        checks X (batch, i) against y (batch, i)
        returns tensor (batch) # of correct 
        """
        return torch.eq(X, y).sum(dim=1)

    @torch.no_grad()
    def validate_accuracy(self, dataloader, model, device='cuda'):
        """Validate the Actual Accuracy of the Model playing Sudoku
        
        dataloader: dataloader responsible for validation data
        model: pytorch model intaking and outputting encoded sudoku features
        device: device for model
        
        returns: torch.tensor sum of the accuracy"""
        model.eval()
        acc = torch.zeros((1)).to(device)
        for batch, (X, y) in enumerate(dataloader):
            X, y = X.to(device), y.to(device)
            acc += self.board_check(
                X = torch.argmax(model(X), dim=2),
                y = torch.argmax(y, dim=2)
            ).sum() / X.size(0)    
        acc /= 81 * (batch + 1)
        print(f'Accuracy: {acc.item():0f}')
        return acc