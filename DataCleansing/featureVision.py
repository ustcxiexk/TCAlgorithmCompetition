import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Author: XXK
Version: 0.11
LastChange: ZXH
LastChangeTime: 8.15 4/20
'''

df = pd.read_csv('./Data/train.csv')
rows, cols = df.shape[0], df.shape[1]
print (rows, cols)
df1, df2 = df[df['label']==1], df[df['label']==-1]
numOfPos = df1.shape[0]
numOfNeg = df2.shape[0]
print (numOfPos, numOfNeg)

#整体及部分均衡性图
plt.subplot(211)
labels = ['SeedUser', 'NonSeedUser']
sizes = [numOfPos/rows, 1 - numOfPos/rows]
patches,l_text,p_text = plt.pie(sizes,labels=labels,autopct = '%3.1f%%',shadow = False,
                                startangle = 90)


a = df[['aid', 'uid', 'label']].groupby(['aid','label']).count()
d = {}
for (aid, label), count in a.itertuples():
    if aid not in d:
        d[aid] = count
    else:
        d[aid] = count / (count + d[aid])

# aid -> 'label == 1'%
plt.subplot(223)
plt.xlabel('aid')
plt.ylabel('Seed/NonSeed Ratio')
pd.Series(d).plot()
# len(aid) -> 'label == 1'%
plt.subplot(224)
plt.xlabel('n-th')
plt.ylabel('Seed/NonSeed Ratio')
pd.Series(list(d.values())).plot()
plt.show()
