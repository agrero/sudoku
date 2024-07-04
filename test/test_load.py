import unittest

import os
import pandas as pd
import numpy as np

import torch
from torch.utils.data import DataLoader

import torch.nn as nn

from sudoku.classes.loader.SudokuDataset import SudokuDataset
from sudoku.classes.nn.ConvNN import ConvNN

from collections import Counter


class TestLoad(unittest.TestCase):

    # SETUP AND TEARDOWN
    # all of this should be read in from a config file
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'testing: {cls.__module__}')
        cls.parent_path = os.path.join('data', 'test')
        cls.data_path = os.path.join(cls.parent_path, 'test_data.parquet')
        cls.sol_path = os.path.join(cls.parent_path, 'test_solutions.parquet')
        cls.model_path = os.path.join('data','models','model_current.pt')

        cls.data = pd.read_parquet(cls.data_path)
        cls.sol = pd.read_parquet(cls.sol_path)

        cls.batch_size = 5
        cls.dataloader = DataLoader(
            SudokuDataset(
                cls.data.to_numpy(),
                cls.sol.to_numpy()
            ),
            batch_size = cls.batch_size
        )

        cls.device = 'cuda'

        cls.model = ConvNN().to(cls.device)
        cls.model.load_state_dict(torch.load(cls.model_path))

        cls.model_count = Counter(
            [type(module) for module in cls.model.modules() 
             if not isinstance(module, nn.Sequential)]
        )
        cls.model_count = [count for count in cls.model_count.values()]
        cls.model_countlabel = [1, 16, 15, 17, 2, 1]
        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')

    # TESTS

    def test_loadparquet(self):
        self.assertEqual(self.data.shape,(10, 81))
        for row in self.data.dtypes:
            self.assertTrue(row == np.int16)

    def test_dataloader(self):
        # Check output shapes from batched dataloader
        for batch, (X, y) in enumerate(self.dataloader):
            X, y = X.to(self.device), y.to(self.device)
            self.assertTrue(X.shape == torch.Size([self.batch_size,81]))
            self.assertTrue(y.shape == torch.Size([self.batch_size,81,9]))

    def test_loadmodel(self):
        # check if correct instance
        self.assertIsInstance(self.model, ConvNN)

        # check for number of model layers
        self.assertEqual(
            self.model_count,
            self.model_countlabel
        )