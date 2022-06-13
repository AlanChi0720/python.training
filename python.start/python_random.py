import random

data = random.choice([1,5,6,10,20])
data1 = random.sample([1,5,6,10,20], 3)

data2 = [1,5,8,20]
random.shuffle(data2) # 洗牌

data3 = random.random() # 0-1 隨機亂數
data4 = random.uniform(0.0 , 2.0) # n-n 隨機亂數

# 常態分配亂數 ( mean, stdev )
data5= random.normalvariate(0, 5)

import statistics as stat

list1 = [1,2,3,3,3,3,4,5,8,100]
datamean = stat.mean(list1)
datamedian = stat.median(list1)
datastdev = stat.stdev(list1)

print(datamean, datamedian, datastdev)