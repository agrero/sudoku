from sudoku.classes.config.SudokuConfig import SudokuConfig
import os

class ConfigFrame(SudokuConfig):

    def setUp(self):
        self.config_path = '/home/alex/coding-projects/sudoku/test.ini' # to be changed
        self.read_config(verbose=True)