import sys
import random
import numpy as np
import pandas as pd
from haming_practice import haming

df = pd.read_csv('sample.csv', names=['word', 'bin'])

rowCount = len(df.index)
count = 0
for i in range(0, rowCount):
    for j in range(i+1, rowCount):
        hd = haming(df.iloc[i, 1], df.iloc[j, 1])
        print(count, "(", df.iloc[i, 0], df.iloc[j, 0], ")haming_distance: ", hd)
        count = count + 1
        min = sys.maxsize
        if (min > int(hd)):
            min = hd
print("min haming distance", min)
