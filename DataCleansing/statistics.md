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

### 各特征的缺失比例
![Aaron Swartz](https://github.com/ustcxiexk/TCAlgorithmCompetition/blob/master/DataCleansing/images/Missing_Percentage.png)

### 特征之间的相关性
                       aid       uid     label       LBS	      age      carrier  consumptionAbility  education	 gender
aid                 1.000000  0.000249 -0.000006  -0.000658  -0.020100  0.040111   0.043926           0.025987  0.031444
uid                 0.000249  1.000000 0.000090   0.000276   0.000064   -0.000454  -0.000564          0.000383  0.00062
label               -0.000006 0.000090 1.000000   0.000205   -0.026711  -0.010249  0.026574          -0.026587  -0.010236
LBS                 -0.000658 0.000276 0.000205   1.000000   -0.002024  0.001262   0.016074          -0.000379  -0.001033
age                 -0.020100 0.000064 -0.026711  -0.002024  1.000000   -0.047442  -0.066855          0.115542  -0.068568
carrier             0.040111 -0.000454 -0.010249  0.001262   -0.047442  1.000000   0.193915           0.174121  0.020758
consumptionAbility  0.043926 -0.000564 0.026574   0.016074   -0.066855  0.193915   1.000000           0.095281  0.107036
education           0.025987  0.000383 -0.026587  -0.000379  0.115542   0.174121   0.095281           1.000000  -0.000927
gender              0.031444  0.000620 -0.010236  -0.001033  -0.068568  0.020758   0.107036           -0.000927     1

