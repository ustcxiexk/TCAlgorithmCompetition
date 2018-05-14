import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./Data/featuredTrainSlice0.csv')

PROCESS_COLUMN = df.columns.tolist()

mode = df.mode()
d = {col:mode[col][0] for col in PROCESS_COLUMN}
nand = {col:0 for col in PROCESS_COLUMN}
df.replace(nand, np.nan)
df = df.fillna(value=d)

print(df)