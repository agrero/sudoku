import pandas as pd
import os
import numpy as np


def conv_framelist(df:pd.DataFrame, colndx:int = 0, conv:bool=False, batch_size:int = 10000) -> pd.DataFrame:
    """
    Reads in a csv file and converts integer types in order to 
    
    df: dataframe to convert values with
    colndx: column integer to convert (?)
    conv: 
    """
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

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]