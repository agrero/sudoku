import os 
import pandas as pd

from sudoku.classes.LabelEncoder import LabelEncoder


data_path = os.path.join('data', 'puzzles')

solutions_pandas = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
).iloc[0:10, :]

data_pandas = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
).iloc[0:10, :]

le = LabelEncoder(solutions_pandas)
