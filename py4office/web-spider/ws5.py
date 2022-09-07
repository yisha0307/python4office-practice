import re

html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""
#贪婪匹配，re.S可以匹配换行符
#创建正则表达式对象
pattern = re.compile('<div><p>.*</p></div>', re.S)
#匹配html 元素，提取信息
re_list= pattern.findall(html)
print(re_list)

# 非贪婪匹配
pattern1 = re.compile('<div><p>.*?</p></div>',re.S)
re_list1 = pattern1.findall(html)
print(re_list1)  # 更优