import pandas as pd
import json

URL = 'https://static.runoob.com/download/sites.json'
s = pd.read_json(URL)
print(pd.DataFrame(s))

# df.to_excel('py4office/py-pandas/data/new_table.xlsx', sheet_name='json')

df2 = pd.read_json('py4office/py-pandas/data/nested_list.json')
PD_PATH = 'py4office/py-pandas/data/nested_list.json'
# 使用Python JSON载入数据
with open(PD_PATH, 'r') as f:
    data =json.loads(f.read())
df_nested_data = pd.json_normalize(data, record_path=['students'], meta = ['school_name', 'class'])  #record_path用于展开studebts子集
print(df_nested_data)