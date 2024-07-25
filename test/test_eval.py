import os
import unittest
import pandas as pd

import torch
from torch.utils.data import DataLoader

from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.nn.Evaluator import Evaluator
from sudoku.classes.load.SudokuDataset import SudokuDataset


class TestEval(unittest.TestCase):
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'SETTING UP: {cls.__module__}')
        cls.data_path = os.path.join(
            'data', 'test', 'test_data.parquet'
        )
        cls.sol_path = os.path.join(
            'data', 'test', 'test_solutions.parquet'
        )
        cls.model_path = os.path.join(
            'data','models','model_current.pt'
        )
        
        cls.device = 'cuda'

        cls.model = ConvNN().to(cls.device)
        cls.model.load_state_dict(torch.load(cls.model_path))

        cls.dataloader = DataLoader(
            SudokuDataset(
                pd.read_parquet(cls.data_path).to_numpy(),
                pd.read_parquet(cls.sol_path).to_numpy()
            ),
            batch_size=10
        )
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')

    def test_Evaluator(self):
        e = Evaluator()
        # Confusion Matrix 
        e.confusion_matrix(
            dataloader=self.dataloader,
            model=self.model,
            device=self.device
        )

        # Validate Accuracy
        e.validate_accuracy(
            dataloader=self.dataloader,
            model=self.model,
            device=self.device
        )
        