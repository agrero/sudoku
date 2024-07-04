import os
import unittest

import torch

from sudoku.classes.solver.MlSolver import MlSolver

# from sudoku.classes.solver.MlSolver import MlSolver

class TestSolve(unittest.TestCase):
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'SETTING UP: {cls.__module__}')
        cls.model_path = os.path.join(
            'data','models','model_current.pt'
        )

        cls.model = ConvNN().to(cls.device)
        cls.model.load_state_dict(torch.load(cls.model_path))

        cls.device = 'cuda'
        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')

    def test_MlSolver(self):
        solver = MlSolver(device=self.device)
        solver.solve_by_parts(self.model, self.data)
        print(sum(solver.accuracies) / len(solver.accuracies))


