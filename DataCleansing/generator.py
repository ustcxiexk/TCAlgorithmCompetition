# coding=utf-8
import pandas as pd
import os

'''
Version: 0.1
LastChange: ZXH
LastChangeTime: 08.04 4/20
'''

# Generate userFeature
ad_feature=pd.read_csv('./Data/adFeature.csv', nrows = 100)
if os.path.exists('./Data/userFeature.csv'):
    print('userFeature Already Exist')
    user_feature=pd.read_csv('./Data/userFeature.csv', nrows = 100)
else:
    userFeature_data = []
    print('Generating userFeature...')
    with open('./Data/userFeature.data', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip().split('|')
            userFeature_dict = {}
            for each in line:
                each_list = each.split(' ')
                userFeature_dict[each_list[0]] = ' '.join(each_list[1:])
            userFeature_data.append(userFeature_dict)
            if i % 100000 == 0:
                print(i)
        user_feature = pd.DataFrame(userFeature_data)
        del userFeature_data # release memory
        user_feature.to_csv('./Data/userFeature.csv', index=False)

# Generate featuredTrain
dfTrain = pd.read_csv('./Data/train.csv', nrows = 100)
train_merged = pd.merge(dfTrain,user_feature,how='left',on='uid')
train_merged.to_csv('./Data/featuredTrain.csv')
del dfTrain # release memory

temp_list = [[] for i in range(10)]
for name, group in train_merged.groupby('aid'):
    temp_list[int(name) % 10].append(group)
for index, groups in enumerate(temp_list):
    file_name = './Data/featuredTrainSlice' + str(index) + '.csv'
    pd.concat(groups).to_csv(file_name)
del temp_list # release memory

# Generate featuredTest
dfTest1 = pd.read_csv('./Data/test1.csv', nrows = 100)
test1_merged = pd.merge(dfTest1,user_feature,how='left',on='uid')
test1_merged.to_csv('./Data/featuredTest1.csv')
del dfTest1 # release memory

del user_feature # release memory



