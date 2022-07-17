# 标准库
# random
import random
t = random.choice(['1', 'erw',' sfd'])
print('-'*30, t)

p = random.sample(range(100), 10)
print(p)
print(random.random())  #random float
print(random.randrange(6))  #random integer chosen from range(6)

#statistics
import statistics
data = [2.75, 1.75, 3, 8.56, 5.24, 3.87]
m1 = statistics.mean(data)  # 均值
m2 = statistics.median(data)  #中位数
m3 = statistics.variance(data)  #方差
print('m1:', m1, 'm2:', m2, 'm3:', m3)

from datetime import date
now = date.today()
print(now)

birthday = date(1990,3,7)
age = now - birthday
print(age.days)