from turtle import pos, position
from unittest import result
import numpy as np

ints = [1,4,5,4,5,2,3,3,3]
unique_arr = sorted(set(ints))
print(unique_arr)

values = np.array([6,7,5,1,1,0,0,9,2])
result = np.in1d(values, [4,5,6])
print(result)

# arr = np.random.randn(5,5)
# np.save('some_array', arr)

raw_arr = np.load('some_array.npy')
print(raw_arr)

import random
import matplotlib.pyplot as plt
position = 0
steps = 1000
walk = [position]
for i in range(1000):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

# plt.plot(walk[:100])

# 等同于：
nstep = 1000
draws = np.random.randint(0, 2, size=nstep)
steps = np.where(draws >0, 1, -1)
walk = steps.cumsum()
print(len(walk), walk.min(), walk.max())

rr = (np.abs(walk) >= 10).argmax()
print(rr)