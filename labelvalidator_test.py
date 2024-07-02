from sudoku.classes.labels.LabelValidator import LabelValidator

import os
import pandas as pd

data_path = os.path.join('data', 'puzzles')
data = pd.read_parquet(
    os.path.join(data_path, 'puzzles_3m.parquet')
)
solutions = pd.read_parquet(
    os.path.join(data_path, 'solutions_3m.parquet')
)


val = LabelValidator(data, labels=solutions)
val.validate()

val.labels.to_parquet(
    os.path.join(data_path, 'fsolutions_3m.parquet')
)