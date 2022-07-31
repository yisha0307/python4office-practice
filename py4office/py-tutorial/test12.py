import pandas as pd
import numpy as np

# pd.read_html可以读所有<table>标签里的数据，转成dataframe
tables = pd.read_html('py4office/py-tutorial/data/fdic_failed_bank_list.html')

failures = tables[0]
close_timestapes = pd.to_datetime(failures["Closing Date"])

aa = close_timestapes.dt.year.value_counts()
print(aa)