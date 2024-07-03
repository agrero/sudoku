from argparse import ArgumentParser
from sudoku.classes.config.SudokuConfig import SudokuConfig
import os


class SudokuMain(ArgumentParser, SudokuConfig):
    def __init__(self, **kwargs):
        self.prog='Program'
        self.description='Parsin some args'
        self.epilog='text where the joke should go'
        for key, value in kwargs.items():
            setattr(self, key, value)

        super().__init__(self)


    # these should probably go in a argparser wrapper
    def add_args(self):
        self.add_argument('-f' ,'--filepath')
        self.add_argument('-c', '--config_path')
        self.add_argument('-t', '--test')
        self.add_argument('-w', '--write_config', action='store_true')

    def set_args(self):
        for key, value in self.parse_args().__dict__.items():
            setattr(self, key, value)
    
    def print_args(self):
        for key, value in self.parse_args().__dict__.items():
            print(f'{key} : {value}')

    def write_config(self):
        return super().write_config(self.config_path)

    def main(self):
        print('Starting main\n')
        self.print_args()
        if self.write_config:
            # requires self.config_path kwarg
            print('write')

if __name__ == '__main__':

    config_path = os.path.join('configs', 'config.ini')
    main = SudokuMain(config_path=config_path)
    main.add_args()
    main.set_args()
    main.main()


