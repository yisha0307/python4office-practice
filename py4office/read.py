import xlrd
# xlrd 2.0.1不支持xlsx，需要安装xlrd 1.2.0及更早版本
# pip install xlrd==1.2.0

xlsx = xlrd.open_workbook('py4office/7月下旬入库表.xlsx')

sheet = xlsx.sheet_by_index(0)

print(sheet.cell_value(0,0))