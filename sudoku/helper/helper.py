import pandas as pd
import os
import numpy as np


def conv_framelist(df:pd.DataFrame, colndx:int = 0, conv:bool=False, batch_size:int = 10000) -> pd.DataFrame:

    for i in range(0, df.shape[0], batch_size):

        # format string to int
        print('creating list from dataframe column')
        data = df.iloc[i:i+batch_size,colndx].apply(
            lambda x: [int(i) if i != '.' else 0 for i in x]
        )
        # return new dataframe

        print('creating new dataframe')

        data = pd.DataFrame(
            [np.array(i) for i in data.to_numpy()]
        )

        # data.columns = data.rename(str, axis='columns')

        print('converting columns to int16')
        if conv:
            for col in data.select_dtypes(include=['int64']).columns:
                data[col] = data[col].astype('int16')

        print('saving chunk')

        data.to_parquet(
            os.path.join('data', 'puzzles', f'puzzle-{i:07}.parquet')
            )

def generate_dumby_data():
    # this is wrong change!
    """Generates all possible values for sudoku solver labels
    shape should be (batch, 729) after one hot encoding
    
    returns: pandas dataframe of size 9x81 such that every label value is accounted for
    """
    return pd.DataFrame(
        [[j for i in range(81)] for j in range(10)]
    )

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]