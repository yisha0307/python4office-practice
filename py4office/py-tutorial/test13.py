import pandas as pd

link = 'py4office/py-tutorial/data/ex1.xlsx'
# xlsx = pd.ExcelFile(link)
# sheet_one = pd.read_excel(xlsx, 'Sheet1')
# print(sheet_one)

# OR:
sheet_one = pd.read_excel(link, 'Sheet1')
print(sheet_one)

frame = sheet_one[['a', 'b', 'c', 'd']] * 2
print(frame)
frame.to_excel(link, 'Sheet2')