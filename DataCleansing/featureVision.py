import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
rows, cols = df.shape[0], df.shape[1]
print (rows, cols)
df1, df2 = df[df['label']==1], df[df['label']==-1]
numOfPos = df1.shape[0]
numOfNeg = df2.shape[0]
print (numOfPos, numOfNeg)

# plt.figure(figsize=(6,9))
labels = ['SeadUser', 'NonSeadUser']
sizes = [numOfPos/rows, 1 - numOfPos/rows]
patches,l_text,p_text = plt.pie(sizes,labels=labels,autopct = '%3.1f%%',shadow = False,
                                startangle = 90)
plt.show()


# print (df)
# print(df1[['label']].apply(sum))
# print(df2[['label']].apply(sum))

# print(df.apply(sum))
