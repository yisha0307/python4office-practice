import re

# enumerate()
# 遍历一个序列的同时追踪当前元素的索引
arr = list('skdjfew')
obj={}
for i, v in enumerate(arr):
    obj[i]=v
print(obj)

# 三元表达式
# value = true-value if condition else false-value
x = 5
vv = 'true' if x < 4 else 'false'
print(vv)

tup = [(1,2), (3,4), (5,6), (7,8)]
# 平铺嵌套列表
arr1 = [x for item in tup for x in item]
print(arr1)
# 嵌套列表推导式
arr2 = [[x for x in item] for item in tup]
print(arr2)

# 函数是对象
def remove_puctuation(value):
    return re.sub('[?#!', '', value)
clean_ops = [remove_puctuation, str.strip, str.title]
# 清理数据
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
# 或者是
def clear_strings(strings, ops):
    result = []
    for function in ops:
        result = map(function, strings)
    return result

# 匿名函数 lambda
ann = lambda x:x*2
arr = [2,4,5]
arr_list = list(map(ann, arr))
print(arr_list)

