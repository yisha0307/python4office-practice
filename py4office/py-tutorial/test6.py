## chapter 4 numpy
import numpy as np
my_arr = np.arange(10)
print(my_arr)

data = np.random.randn(2,3)
print(data)

print(data * 100)
print(data + data)
print(data.shape)

data2 = np.empty((2,3,2))
print(data2)
print(np.zeros((2,3)))

arr = np.array([[1,2,3],[4,5,6]])
arr2 = arr + arr
arr3 = arr * arr
arr4= arr - arr
print(arr2, arr3, arr4)
print('-'*40)

# 布尔索引（true才有，false就去掉）
data2 = np.random.randn(4,5)
# print(data2)
names = np.array(['bob', 'allen', 'emily', 'lily'])
ab = data2[names == 'bob', 2:5]
print(ab)

mask = (names == 'bob') | (names == 'emily')
print(mask)
print(data2[mask,2:])

data2[data2 <0] = 0
print(data2)
print('-'*40)

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i + 2
print(arr)
bb = arr[[4,3,0,6], :2]
print(bb)

arr2 = np.arange(32).reshape(8,4)
print(arr2)

arr3 = arr2[[1,3,7,5],[3,2,0,1]]
print(arr3)