import pandas as pd
import numpy as np
import matplotlib as plt
import fileinput

DEBUG = 1

column = pd.Series([
    'uid',
    'age',
    'gender',
    'marriageStatus',
    'education',
    'consumptionAbility',
    'LBS',
    'interest1',
    'interest2',
    'interest3',
    'interest4',
    'interest5',
    'kw1',
    'kw2',
    'kw3',
    'topic1',
    'topic2',
    'topic3',
    'appIdInstall',
    'appIdAction',
    'ct',
    'os',
    'carrier',
    'house'
])
dfData = pd.DataFrame(columns=column)

tempdf = []
cnt = 0
with fileinput.input(files=r'userFeature.data') as f:
    for line in f:
        d = {}
        for tmpstring in line.strip().split('|'):
            l = tmpstring.split()
            d[l[0]] = [int(i) for i in l[1:]] if len(l) > 2 else int(l[1])

        if DEBUG:
            print(line, d)

        tempdf.append(d)
        cnt += 1

        if DEBUG:
            if cnt >= 10:
                dfData = pd.concat([dfData, pd.DataFrame(tempdf, columns=column)])
                break            
        else:
            if not (cnt % 10000):
                print(cnt, 'lines processed')
                dfData = pd.concat([dfData, pd.DataFrame(tempdf, columns=column)])
            
if DEBUG:
    print(dfData)
dfData.to_csv(r'Data.csv')