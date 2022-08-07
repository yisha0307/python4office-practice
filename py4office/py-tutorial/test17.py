import pandas as pd
import numpy as np
from pyparsing import col

data = pd.read_csv('py4office/py-tutorial/data/macrodata.csv')
print(data.head())

periods = pd.PeriodIndex(year = data.year, quarter = data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns = columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0:'value'})
print(ldata.head(10))