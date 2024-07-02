from sudoku.classes.solver.Solver import Solver
from sudoku.classes.Board import Board

import numpy as np

class LabelValidator(Solver):
    def __init__(self, data, labels) -> None:
        super().__init__(Board=Board)
        self.data = data.to_numpy()
        self.labels = labels.to_numpy()

    def validate(self, batch_print=5):
        """
        Validates labels by using a backtracking algorithm.
        Overwrites label entry if incorrect.

        * SHOULD ADD A BATCH SAVING MECHANIC LATER *
        * MIGHT BE FUN PRACTICE FOR SOME MULTITHREADING *
        
        returns: pandas dataframe of linearized labels.
        """
        
        for ndx, board in enumerate(self.data):

            self.solve_sudoku(board.reshape((9,9)))
            if not np.array_equal(self.board.flatten(), self.labels[ndx]):
                self.labels[ndx] = self.board.flatten()    

            if ndx % batch_print == 0:
                print(f'Progress: [{ndx+1:-7}/{self.data.shape[0]:07}]')

        return self.labels
