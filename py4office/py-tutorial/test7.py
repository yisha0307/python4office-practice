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