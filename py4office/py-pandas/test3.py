import pandas as pd

DATA_PATH = 'py4office/py-pandas/data/property-data.csv'

# df = pd.read_csv(DATA_PATH).dropna(subset=['ST_NUM'])
df = pd.read_csv(DATA_PATH)
# print(df['ST_NAME'])
# print(df.loc[0])
# print(df)

x = df['ST_NUM'].mean()
print(x)
df['ST_NUM'].fillna(x, inplace=True)
new_df = df.dropna(subset=['PID'])
print(new_df.to_string())

# FORAMT错误数据
data2 = {
    "Date": ['2020/12/01', '2020/12/02' , '20201226'],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data2, index=['day1','day2','day3'])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string()) 
# 修改/删除错误数据
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}

df = pd.DataFrame(person)

for x in df.index:
    if df.loc[x, 'age'] > 120:
        # df.loc[x, 'age'] = 120
        df.drop(x, inplace=True)

print(df.to_string())