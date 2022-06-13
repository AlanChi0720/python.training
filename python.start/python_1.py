s= """Hello
World"""
# triple """   """ == \n
# print(s, sep= "\n")

# 巢狀列表
data= [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
# print(data[1][1][0:3])

# set
s1= {3,4,5}
s2= {4,5,6,7,8}
s3= s1&s2 # 交集
s3= s1|s2 # 聯集 (不重複)
s3= s2-s1 # 差集
s3= s1^s2 # 反交集
# print(s3)
# print(3 in s1, 10 not in s1)
s= set('Hello') # set(str)
# print('H' in s)

dic= {'a':'apple', 'b':"bug" ,'c':'cat'}
del dic['a']

dic={i:i*2 for i in [1,3,4]}
print(dic)