from typing import Mapping


a = list(range(0,20,2))
print(a)
b = list(range(20,0,-2))
print(b)

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a,b)
print(rest)

a = (1, 2,2,2,3,4,5)
print(a.count(2))    #3

words = ['bat', 'baz', 'amo', 'ago', 'lo']
mapping = {}
for word in words:
    i = word[0]
    if i not in mapping:
        mapping[i] = [word]
    else:
        mapping[i].append(word)
print(mapping)

# 以上等同于:
letter_words = {}
for word in words:
    i = word[0]
    letter_words.setdefault(i, []).append(word)
print(letter_words)

# 以上等同于：
from collections import defaultdict
letter_words2 = defaultdict(list)
for word in words:
    i = word[0]
    letter_words2[i].append(word)
print(letter_words2)

#列表推导式
strings = ['a', 'aer','bat', 'gu', 'goat']
result_list = [x.upper() for x in strings if len(x)>2]
print(result_list)

unique_lengths = {len(x) for x in strings}
print(unique_lengths)

loc_mapping = {val: index for index, val in enumerate(strings)}

all_data=[['john', 'emily', 'michael', 'mary','steven'], ['maria', 'juan', 'javier', 'natalia', 'pilar']]
result = []
for names in all_data:
    filtered_names = [name for name in names if name.count('e') >= 2]
    result.extend(filtered_names)
print(result)

# 以上等同于
result2 = [name for names in all_data for name in names if name.count('e') >= 2]
print(result2)

result3 = [name for names in all_data for name in names if name[-1] is 'n']
print(result3)

rlist = [(1,2,3), (4,5,6), (7,8,9)]
flattened_list = [x for tup in rlist for x in tup]
print(flattened_list)

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key = lambda x : len(set(x)))
print(strings)

# 迭代器&&生成器
gen = (x**2 for x in range(100))
print(gen)

def _make_gen():
    for x in range(100):
        yield x **2
gen = _make_gen()
print(gen)
# 直到请求生成器里的代码，才会执行
for x in gen:
    print(x, end=' ')

aa = sum(x ** 2 for x in range(10))
bb = dict({(i, i** 2) for i in range(10)})
print(aa)
print(bb)