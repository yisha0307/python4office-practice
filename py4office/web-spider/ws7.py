# beautiful soup 教程
from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>hello world</p>', 'lxml')
# print(soup.p.string)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.prettify())  # 缩进，并自动更正格式
print(soup.title.string)
print(type(soup.title))
print(soup.head)
print(soup.p)  #只能匹配到第一个节点
print(type(soup.p))
print(soup.p.attrs)
print(soup.p.attrs['name'])

# 获取直接子节点
print(soup.p.contents)

