import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0 ,1])
y = np.empty_like(x)   #生成的是随机数

print(y)

for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

from datetime import datetime, date, time
dt = datetime(2022,10,29,20,30,45)
print(dt)
print(dt.day, dt.minute)