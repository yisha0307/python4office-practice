import csv

with open('eggs.csv', 'w', newline = '') as csvfile:
    # delimeter 指定分隔符，默认为逗号，这里指定为空格
    # quotechar 表示引用符
    # writerow 单行写入，列表格式传入数据
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
    spamwriter.writerow(['www.biancheng.net']*5 + ['how are you'])
    spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])