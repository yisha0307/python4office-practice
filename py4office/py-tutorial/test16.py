from unittest import result
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['ohio', 'colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)

result = data.stack()  # 堆叠
print(result)
print(result.unstack('state'))

s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('cde'))
data2 = pd.concat([s1, s2],keys=['one', 'two'])
print(data2)
print(data2.unstack())
print('-------------')

df = pd.DataFrame({'left': result, 'right': result+5}, columns=pd.Index(['left', 'right'], name='side'))
print(df)

aa = df.unstack('state')
print(aa)
bb = aa.stack('side')
print(bb)
