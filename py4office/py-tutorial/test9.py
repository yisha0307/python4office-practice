import pandas as pd
import numpy as np

obj = pd.Series(['blue', 'red', 'yellow'], index = [0, 2, 4])
obj1 = obj.reindex(range(6), method='ffill')
print(obj1)

df = pd.DataFrame(np.arange(1,10).reshape(3,3), index=np.arange(1,4,1), columns=['one', 'two', 'three'])
ccol = ['one', 'two', 'two']
df1 = df.reindex(columns = ccol)
df2 = df.loc[[2, 2, 3], ccol]
print(df[1:2])
print(df2)

df3 = pd.Series([1, 2, 3, 4], index=['aa','bb','cc','dd'])
print(df3)
print('---------------')
print(df3['aa':'cc'])

data = pd.DataFrame(np.arange(16).reshape(4,4), index=['ohio', 'colorado','utah', 'new york'], columns=['one','two','three','four'])
# print(data)
# print(data['two'])
# print(data[:2])
# print(data[data['three']>5])
# print(data.loc[['colorado','new york']])
# print(data[:1])
print(data > 6)
print('---------------')
# loc选单行多列数据
# 先行后列
aa = data.loc['ohio', ['one', 'two']]
print(aa)
bb = data.iloc[0, [3,1,2]]
print(bb)
cc = data.loc[['ohio','utah'], ['one', 'two']][data['two']>7]
print(cc)
dd=data.at['ohio','one']
print(dd)