import pandas as pd

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
# if not isinstance(obj,list) and isiterable(obj):
#     obj = list(obj)


def add_sheet(df, path, sheet_name):
    try:
        writer = pd.ExcelWriter(path, mode='a')
    except FileNotFoundError:
        writer = pd.ExcelWriter(path, mode='w')
    df.to_excel(writer, sheet_name)
    writer.save()

# apply函数到arr的每一个值
def apply_to_list(list, func):
    return [func(x) for x in list]
# ins = ['HSIDa','aDOUHW','sifdhwAA']
# print(apply_to_list(ins, str.title))
