# 看某个对象是否能遍历
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# aa = isiterable('akshd')
# print(aa)

# 如果不是列表就转化成列表
# 转化成列表也需要是可遍历的对象（比如字符串什么的) 
if not isinstance(obj,list) and isiterable(obj):
    obj = list(obj)