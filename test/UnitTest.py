from sudoku.classes.config.SudokuConfig import SudokuConfig
from sudoku.classes.loader.SudokuLoader import SudokuLoader

from sudoku.test_package.framework.ConfigFrame import ConfigFrame

import unittest
import os

class UnitTest(ConfigFrame, unittest.TestCase):

    # we just want this to work then we can get cookin
    def test_some_method(self):
        self.assertEqual(
            self.device,
            'cuda'
        )


