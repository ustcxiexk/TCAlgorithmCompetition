import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# s = pd.Series([0,1,2,3,4,1,2,3,1])
# print(s)
# bins = plt.hist(s)
# for b,a in zip(bins[0], bins[1]):
#     plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
# print(bins)
# plt.show()

df = pd.read_csv('./Data/featuredTrainSlice0.csv')

# Mark Value on Graphs
def markValue(bins):
    for b,a in zip(bins[0], bins[1]):
        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)

# ---Correlation Analysis---
corr1 = df.corr(method = 'pearson')['label'].drop(['label','aid','uid','Unnamed: 0'])
corr2 = df.corr(method = 'kendall')['label'].drop(['label','aid','uid','Unnamed: 0'])
corr3 = df.corr(method = 'spearman')['label'].drop(['label','aid','uid','Unnamed: 0'])
plt.title('Correlation Analysis')
plt.subplot(311)
corr1.plot()
plt.subplot(312)
corr2.plot()
plt.subplot(313)
corr3.plot()
plt.show()

# ---LBS Scatter---
plt.title('LBS Scatter')
plt.scatter(df['aid'], df['LBS'], s=5, alpha=0.5, edgecolors= 'white')
plt.show()

# ---Histograms---
for string in ['age', 'carrier', 'consumptionAbility', 'education', 'gender']:
    tempdf = df[string]

    plt.subplot(211)
    plt.title(string + ' Histogram')
    bins = plt.hist(tempdf, bins=tempdf.max()-tempdf.min()+1, align='mid',range=(tempdf.min()-0.5,tempdf.max()+0.5))
    markValue(bins)

    plt.subplot(223)
    tempdfS = df[df['label'] == 1][string]
    bins = plt.hist(tempdfS, bins=tempdfS.max()-tempdfS.min()+1, align='mid',range=(tempdfS.min()-0.5,tempdfS.max()+0.5))
    markValue(bins)

    plt.subplot(224)
    tempdfU = df[df['label'] == -1][string]
    bins = plt.hist(tempdfU, bins=tempdfU.max()-tempdfU.min()+1, align='mid',range=(tempdfU.min()-0.5,tempdfU.max()+0.5))
    markValue(bins)

    plt.show()

# --- Missing Percentage ---
xlabel = [i for i in df.axes[1][1:]]
ylabel = [(1 - df[label].count() / len(df)) * 100 for label in xlabel]
s = pd.Series(ylabel, index=xlabel)
s.plot.bar()
plt.title('Missing Percentage')
bins = [ylabel, range(len(xlabel))]
markValue(bins)
plt.show()