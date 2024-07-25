import pandas as pd

def hilo_thresh_feature(data, hi, lo, feature):
    return data[(data.loc[:,feature] >= lo) & (data.loc[:,feature] <= hi)]