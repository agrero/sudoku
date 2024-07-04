import unittest
from sudoku.classes.nn.ConvNN import ConvNN
from sudoku.classes.loader.SudokuDataset import SudokuDataset
from sudoku.classes.nn.Trainer import Trainer
from sudoku.classes.labels.LabelEncoder import LabelEncoder

import torch
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch.optim import Adam

import os
import pandas as pd

class TestModel(unittest.TestCase):

    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'SETTING UP: {cls.__module__}')
        
        # PATHS
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

        cls.optimizer = Adam(cls.model.parameters(), lr=1e-2)
        cls.loss_fn = CrossEntropyLoss().to(cls.device)

        cls.trainer = Trainer()
        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')

    def test_train_norm(self):
        # run a training iteration
        self.trainer.train_norm(
            dataloader=self.dataloader,
            model=self.model,
            loss_fn=self.loss_fn,
            optimizer=self.optimizer,
            device=self.device
        )

    def test_LabelEncoder(self):
        self.assertEqual(
            LabelEncoder(
                pd.read_parquet(self.sol_path).to_numpy()
                ).encode_labels().shape,
            (810, 9)
        )       
        
