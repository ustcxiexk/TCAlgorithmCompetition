## 特征初步分析
### 年龄
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/age.png)
图中分别对应是所有用户的年龄分布以及种子用户和非种子用户的年龄分布（下面其他特征也是类似）。  
一共有5个年龄段，可推断其呈现正态分布。（注意由于经过加密编码，年龄和数字对应关系不确定，有可能需要调整柱状图位置）

### 性别
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/gender.png)
性别分为男女两项（此处的0表示缺失数据，后面的特征类似）

### 运营商
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/carrier.png)
分为移动、联通、电信和其他。

### 消费能力
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/consumptionAbility.png)
消费能力分为高低两项

### 教育程度
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/education.png)
类似于年龄，呈正态分布

### 地理位置
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/LBS.png)
地理位置也是经过加密编码的一维信息。聚类的问题？

### 各特征的确实比例
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/Missing_Percentage.png)
