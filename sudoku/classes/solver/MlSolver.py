from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.load.SudokuLoader import SudokuLoader
from sudoku.classes.load.SudokuDataset import SudokuDataset
from sudoku.classes.nn.Evaluator import Evaluator

import torch
from torch import cuda
from torch.utils.data import DataLoader

import os


class MlSolver(Evaluator):
    def __init__(self, device):
        super().__init__()
        self.iteration = 0
        self.finished_boards = None
        self.device = device
        self.check_sum = torch.zeros(1).to(self.device)
        self.average = self.check_sum / self.iteration + 1.0
        self.lag = 5
        self.accuracies = []

    def solve_by_parts(self, model, dataloader):

        model.eval()

        for batch, (X, y) in enumerate(dataloader):
            print(f'batch: {batch}')
            self.reset()

            X, y = X.to(self.device), torch.argmax(y,dim=2).to(self.device)

            guessing = True
            while guessing:
                print(f'iteration: {self.iteration}')
                check = torch.eq(X, y+1)

                X[~check] = torch.argmax(
                    model(X),
                    dim=2
                )[~check].to(torch.float32)

                self.check_sum += check.sum()
                guessing = self.evaluate_stuckness(
                    average=self.check_sum/self.iteration,
                    current=check.sum(),
                    lag=self.lag,
                    avg_buffer=3.0,
                    iteration=self.iteration
                )
                self.iteration += 1
            
            self.accuracies.append(
                check.sum().item() / 81.0
            )

    def evaluate_stuckness(self, average, current, iteration, lag=5, avg_buffer=1.0):
        print(average)
        cond1 = average > (current - avg_buffer)
        cond2 = (iteration > lag)
        return not (cond2 and cond1)
    
    def reset(self):
        """reset iteration and # of correct answers over n iterations"""
        self.iteration=1
        self.check_sum=0.0