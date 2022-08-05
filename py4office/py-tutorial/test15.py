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
