
import pandas as pd


def tc2df(result):
    result = str(result).split('\n')
    df = pd.DataFrame([x.split(' ') for x in result[1:]], columns=result[0].split()).set_index('t')
    return df

def last_time_as_series(result):
    result = str(result).split('\n')
    names = result[0].split()[1:]
    values = result[-1].split()[1:]
    values = [float(v) for v in values]
    df = pd.Series(values, index=names)
    return df