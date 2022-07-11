import imp
import pandas as pd
from glom import glom

DATA_PATH = 'py4office/py-pandas/data/nested_deep.json'
df = pd.read_json(DATA_PATH)

#使用glom来访问嵌套在子集里的数据
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
print(data.loc[0])