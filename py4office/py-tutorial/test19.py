import os
import pandas as pd
import numpy as np

path = '/Users/yisha/Desktop/2022年一季度上海市级医院综合绩效简报'
files = os.listdir(path)
print(files[0][-20:])

out_path = 'py4office/py-tutorial/result/result2.xlsx'

with pd.ExcelWriter(out_path) as writer:
    for file in files:
        df = pd.DataFrame(np.random.randn(4,5))
        df.to_excel(writer, sheet_name=file[-20:])

# writer.save()
# writer.close()