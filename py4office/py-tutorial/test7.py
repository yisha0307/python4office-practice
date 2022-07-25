from math import remainder
import numpy as np

arr = np.arange(15).reshape(3,5)
print(arr, arr.T)

arr2 = np.random.randn(7) * 5
print(arr2)
remainder, whole_part = np.modf(arr2)  #np.modf()返回小数部分和整数部分
print(remainder, whole_part)

points = np.arange(10)
xs, ys = np.meshgrid(points, points)
print(xs)
print('---------')
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)

import matplotlib.pyplot as plt
plt.imshow(z, cmap = plt.cm.gray);plt.colorbar()

xarr = np.arange(7)
yarr = np.arange(8,1,-1)
cond = np.array([True, False, False,True,True,False, False])
print([x for x in zip(xarr, yarr, cond)])
print('---------')
result = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]
print(result)

#np.where(condition, x, y) x if condition == True else y
result2 = np.where(cond, xarr, yarr)
print(result2)

arr = np.random.randn(4,4)
print(arr)
my_arr = np.where(arr>0, 2, -2)
print(my_arr)

my_arr2 = np.where(arr > 0, 2, arr)
print(my_arr2)

large_arr = np.random.randn(200)
large_arr.sort()
# print(large_arr)

five_percent = large_arr[int(0.05 * len(large_arr))]
print(five_percent)