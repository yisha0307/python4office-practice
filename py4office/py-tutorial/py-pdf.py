import pytesseract
import numpy as np
import pandas as pd
from numpy import NaN
import re
from zhon.hanzi import punctuation

# 判断是不是能转换成float
def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

img = 'data\88888.png'

data = pytesseract.image_to_string(img, lang='chi_sim').replace('[', '|').replace(']', '|').replace('}', '|').replace('{', '|').replace(',', '.')
data = data.split('\n')
data = [x for x in data if len(x)]
# print(data)
data = data[7:]
table = np.zeros([100,20])
for index in range(len(data)):
    line = data[index].split('|')
    # 去除中文
    line = [re.sub('[\u4e00-\u9fa5]', '', x) for x in line]
    # 去除英文字符
    line = [re.sub('[a-zA-Z]', '', x) for x in line]
    # 去掉中文字符
    line = [re.sub('[{}]'.format(punctuation), '', x) for x in line]
    # 去掉小数点后面的空格
    line = [x.replace('. ', '.') for x in line]
    # 去除两边的空格
    line = [x.strip() for x in line]
    # 把没有|的数据分开
    line = [x.split(' ') for x in line]   # 用空格分开
    line = [j for x in line for j in x]   # 平铺二维数组
    line = [x for x in line if x]   # 去掉空值

#     # line = [x.strip().replace(' ', '').replace("'",'').replace('_', '') for x in data[index].split('|')]
    # 实在识别不出来的数据改成nan
    line = [isfloat(x) and x or NaN for x in line]
    # print(line)
    for id in range(len(line)):
        table[index][id] = line[id]

# print(table)
df = pd.DataFrame(table)
df.to_excel('result\/test2.xlsx')
