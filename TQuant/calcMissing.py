#!/bin/python3

import pandas as pd
import numpy as np



#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#

def calcMissing(readings):
    # Write your code here
    df = pd.DataFrame([sub.split("\t") for sub in readings], columns=['TimeStamps', 'Readings'])
    df.loc[df['Readings'].str.contains('Missing'), 'Readings'] = np.nan
    inds = df.loc[pd.isna(df["Readings"]), :].index
    df['Readings'] = df['Readings'].astype(float)
    if np.isnan(df['Readings'][0]):
        df.at[0,'Readings'] = df['Readings'].mean()
    df = df.interpolate()
    # df = df.interpolate(limit=1, limit_direction="backward")
    # print(df.head(50))
    for i in inds:
        print(df['Readings'][i])


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
