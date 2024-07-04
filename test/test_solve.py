import os
import unittest
import pandas as pd

import torch
from torch.utils.data import DataLoader

from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.solver.MlSolver import MlSolver
from sudoku.classes.load.SudokuDataset import SudokuDataset

# from sudoku.classes.solver.MlSolver import MlSolver

class TestSolve(unittest.TestCase):
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'SETTING UP: {cls.__module__}')
        cls.model_path = os.path.join(
            'data','models','model_current.pt'
        )
        cls.sol_path = os.path.join(
            'data', 'test', 'test_solutions.parquet'
        )
        cls.data_path = os.path.join(
            'data', 'test', 'test_data.parquet'
        )

        cls.device = 'cuda' # change to check later

        cls.dataloader = DataLoader(
            SudokuDataset(
                pd.read_parquet(cls.data_path).iloc[:1,:].to_numpy(),
                pd.read_parquet(cls.sol_path).iloc[:1,:].to_numpy()
            ),
            batch_size=1
        )
        cls.model = ConvNN().to(cls.device)
        cls.model.load_state_dict(torch.load(cls.model_path))

        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')

    def test_MlSolver(self):
        solver = MlSolver(device=self.device)
        solver.lag = 2
        solver.solve_by_parts(self.model, self.dataloader)
        print(sum(solver.accuracies) / len(solver.accuracies))


