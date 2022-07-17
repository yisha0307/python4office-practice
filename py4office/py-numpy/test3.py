import numpy as np

# 缺省索引
a= np.arange(0, 100, 10)
b = a[:5]
c = a[a>=50]
print(b)
print(c)

#where函数
a = np.arange(0, 100, 10)
b = np.where(a<50)
c = np.where(a>=50)[0]