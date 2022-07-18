import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])
print(a)
print(b)
print(b.shape)

c = np.random.random((2,2))
print(c)

d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
e = d[:2, 1:3]
print(e)  #[[2,3], [6,7]]