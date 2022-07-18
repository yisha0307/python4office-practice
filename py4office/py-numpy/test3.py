import numpy as np
from math import sqrt

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

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('{0} {1}'.format(idx+1, animal))

a = [1, 2, 3, 4, 5]
b = [i**2 for i in a if i % 2 == 0]
print(b)

b = {'person': 2, 'dog': 4, 'spider':8}
for animal, legs in b.items():
    print('%s has %d legs' % (animal, legs))
    print('{0} has {1} legs'.format(animal, legs)) #same as before

even_num_to_square = {x: x**2 for x in a if x % 2 == 0}
print(even_num_to_square)

nums = {int(sqrt(x)) for x in range(30)}
print(nums)  #集合是没有重复的，元组也一样

#元组
# 元组可以作为字典中的键和集合的元素
d = {(x, x+1): x for x in range(10)}
# print(d)
t = (5,6)
print(t in d)
print(d[(1, 2)])