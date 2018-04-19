import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Author: XXK
Version: 0.11
LastChange: ZXH
LastChangeTime: 14:46 4/19
'''

df = pd.read_csv('train.csv')
rows, cols = df.shape[0], df.shape[1]
print (rows, cols)
df1, df2 = df[df['label']==1], df[df['label']==-1]
numOfPos = df1.shape[0]
numOfNeg = df2.shape[0]
print (numOfPos, numOfNeg)

# 'label == 1' %
labels = ['SeadUser', 'NonSeadUser']
sizes = [numOfPos/rows, 1 - numOfPos/rows]
patches,l_text,p_text = plt.pie(sizes,labels=labels,autopct = '%3.1f%%',shadow = False,
                                startangle = 90)
plt.show()

a = df[['aid', 'uid', 'label']].groupby(['aid','label']).count()
d = {}
for (aid, label), count in a.itertuples():
    if aid not in d:
        d[aid] = 1
    if label == 1:
        d[aid] *= count
    elif label == -1:
        d[aid] /= count

# aid -> 'label == 1'%
pd.Series(d).plot()
plt.show()
# len(aid) -> 'label == 1'%
pd.Series(list(d.values())).plot()
plt.show()


