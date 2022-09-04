# numpy基础
import numpy as np

# numpy两个等尺寸的数组之间可以直接批量操作而无需for循环
arr = np.arange(10)
arr1 = np.arange(2, 22, 2)
print(arr, arr1)
# 不需要for循环
print(arr + arr1)
print(arr1 - arr)
print(1/arr)
# 同尺寸的数组比较，会产生一个布尔值的数组
print(arr1 > arr)

# 布尔值数组对np.array的每一列或者每一行设置数据：
aa = np.random.rand(3,4)
print(aa)
aa[aa < 0.5] = 0.5  # 比如数据处理的时候可以把小于0或者不是数字的数据处理一下
print(aa)

# 神奇索引
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)
# 神奇索引：一次选中多行
picked = arr[[4,3,7,1]]
print(picked)
