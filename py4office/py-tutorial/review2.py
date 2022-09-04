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

# 通用函数（快速的逐元素数组函数）
rrr = np.arange(10)
# 一元通用函数 np.method(x) @x：np.narray
print(np.sqrt(rrr)) # 平方根， 还有类似np.exp(x), np.abs(x)， np.ceil(x), np.floor(x)等, 详见p108
# 二元通用函数 np.method(x,y) @x,y: np.narray
result = np.add(rrr, rrr)  # 元素逐个相加，还有np.subtract(x,y), np.multiply/divide/power/maximum/minimum... 详见p108
print(result)

# 将条件逻辑作为数组操作
xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False, True, False, False])
resull = np.where(cond, xarr, yarr)  # np.where(condition, true-value, false-value) 有点类似 true-value if condition else false-value
print(resull)

# 数学和统计方法 详见p111
rawarr = np.random.randn(5, 4)
aa = rawarr.mean()  # 求所有数字的平均值
bb = np.mean(rawarr)
print(aa, bb)
cc = np.sum(rawarr) # 求所有数字的总和
print(cc)

dd  = np.mean(rawarr, axis=1) #加上axis = 0或者1可以算出每列或者每行上的平均值 np.sum(arr, axis=0) 每一列的和
print(dd)  # 还有arr.cumsum() 和arr.cumprod()