from sudoku.classes.Solver import Solver
from sudoku.classes.Board import Board

import numpy as np

class LabelValidator(Solver):
    def __init__(self, data, labels) -> None:
        super().__init__(Board=Board)
        self.data = data.to_numpy()
        self.labels = labels.to_numpy()

    def validate(self):
        """
        Validates labels by using a backtracking algorithm.
        Overwrites label entry if incorrect.
        
        returns: pandas dataframe of linearized labels.
        """
        
        for ndx, board in enumerate(self.data):

            self.solve_sudoku(board.reshape((9,9)))
            if not np.array_equal(self.board.flatten(), self.labels[ndx]):
                self.labels[ndx] = self.board.flatten()    

        return self.labels
