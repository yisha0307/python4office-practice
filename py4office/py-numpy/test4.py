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

aa = np.array([[1,2], [3,4], [5,6]])
bb = aa[[0, 1, 2], [0, 1, 0]]
print(bb)
cc = [aa[0,0], aa[1,1], aa[2,0]]
print(cc)

dd = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(dd)
ee = dd[np.arange(4), np.array([0,2,0,1])]
print(ee)  #[1, 6, 7, 11]
dd[np.arange(4), np.array([0, 2, 0 ,1])] += 10
print(dd)

#布尔索引
bool_idx = dd > 5
print(bool_idx)
# [[ True False False]
#  [False False  True]
#  [ True  True  True]
#  [ True  True  True]]
print(dd[bool_idx])
print(dd[dd > 10])

x = np.array([[1,2], [3,4]])
print(np.sum(x, axis=0))  # sum of each column [4, 6]
print(np.sum(x, axis=1))  # sum of each row [3, 7]

# 转置
print(x.T)