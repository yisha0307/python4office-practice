from timeit import timeit
from common import add_sheet
import pandas as pd

# 三元表达式
# value = true-value if condition else false-value
x = 5
aa = 'none-negative' if x >=0 else 'negative'
print(aa)

# 元组tuple
seq = [(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in seq:
    print('a={0}, b= {1}, c={2}'.format(a,b,c))

values = 1,2,3,4,5
a,b,*s = values
print(a)
print(b)
print(s)  # [3,4,5]

path = 'py4office/py-tutorial/result/result3.xlsx'
result2=[('a','2','ss'),('b','2','33'),('c','4','bbb')]
df = pd.DataFrame(result2, columns=list('abc'))
add_sheet(df, path, 'add')