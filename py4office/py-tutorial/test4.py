import itertools


# itertools 模块
import itertools
first_letter = lambda x: x[0]
names = ['alan', 'group', 'ali', 'wes', 'wills','steven']
names = [x.title() for x in names]
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))

#错误和异常处理
def attemp_float(x):
    try:
        return float(x)
    except:
        return x
result1 = attemp_float('5.66')
result2 = attemp_float('asd')
print(result1, result2)

#抓特定的错误
def attemp_float2(x):
    try:
        print(float(x))
    except ValueError:
        print(x)
attemp_float2('3.445')
attemp_float2('sdufgiawe')
# attemp_float2((3,4))

import sys
ab = sys.getdefaultencoding()
print(ab)