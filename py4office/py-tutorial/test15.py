from unittest import result
import pandas as pd
import numpy as np
from pyparsing import col

left = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left, '\n', right)

mm = pd.merge(left, right, left_on='key', right_index=True)
print(mm)

left1 = pd.DataFrame({'key1': list('OOONN'), 'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5.)})
right1 = pd.DataFrame(np.arange(12).reshape(6,2), index = [list('NNOOOO'),[2001, 2000, 2000, 2000, 2001, 2002]], columns=['e1', 'e2'])
print(left1)
print(right1)

mm1= pd.merge(left1, right1, left_on = ['key1', 'key2'], right_index=True, how='outer')
print(mm1)

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index = ['a', 'c', 'e'], columns=['ohio', 'nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.],[13., 14.]], index = list('bcde'), columns=['mixxx', 'Alama'])
print(left2)
print(right2)
mm2 = pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
print(mm2)

mm3 = left2.join(right2, how='outer')
print(mm3)

# 延轴线堆叠
arr = np.arange(12).reshape(3,4)
print(arr)

aa = np.concatenate([arr, arr], axis=1)
print(aa)
bb = np.concatenate([arr, arr])  # 默认axis = 0
print(bb)

s1 = pd.Series([0, 1], index = ['a', 'b'])
s2 = pd.Series([2,3,4], index = ['c','d','e'])
s3 = pd.Series([5,6], index=['f', 'g'])
cc = pd.concat([s1, s2, s3])  # concatenate是np的接口，concat是pd的接口
print(cc)
dd = pd.concat([s1,s2,s3], axis=1)
print(dd)

result = pd.concat([s1, s1, s3], keys=['s1', 's2', 's3'])  # keys可以在结果中区分
print(result)
print(result.unstack())
print('---------------')

df1 = pd.DataFrame(np.arange(6).reshape(3,2), index=list('abc'), columns=['one', 'two'])
df2 = pd.DataFrame(5+np.arange(4).reshape(2,2), index=['a','c'], columns=['three', 'four'])
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=0))
result1 = pd.concat([df1, df2], axis=1, keys=['df1', 'df2'],names=['up','down'])
print(result1)
print('---------------')

df3 = pd.DataFrame(np.random.randn(3,4), columns=list('abcd'))
df4 = pd.DataFrame(np.random.randn(2,3), columns=list('bda'))
print(df3, '\n', df4)
rr = pd.concat([df3, df4], ignore_index=True)
print(rr)

a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan], index = list('fedcba'))
b = pd.Series([0., np.nan, 2., np.nan, np.nan, 5.], index = list('abcdef'))
print(a)
print(b)
print('---------------')
mmm = np.where(pd.isnull(a), b, a)  #np.where(condition, x, y) condition成立时返回x，否则y
print(mmm)

# combine_first(): 用来补缺失值
abb = b.combine_first(a)
print(abb)
print(a.combine_first(b))


