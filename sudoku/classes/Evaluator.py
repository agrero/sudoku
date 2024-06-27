from sudoku.classes.ConvNN import ConvNN
from sklearn.metrics import confusion_matrix

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
            
            if batch >= 10:
                break
        return conf_matrix
    
