
import pandas as pd


def tc2df(result):
    result = str(result).split('\n')
    df = pd.DataFrame([x.split(' ') for x in result[1:]], columns=result[0].split()).set_index('t')
    return df