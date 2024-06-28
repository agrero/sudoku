import pandas as pd

def filter_hilo(data, hi, lo):
    return data[(data.index >= lo) & (data.index <= hi)]