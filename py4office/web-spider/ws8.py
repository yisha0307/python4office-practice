html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.p.children)
# print(list(soup.p.children))
# for i in soup.p.children:
#     print(i)
# print(soup.p.descendants)
# for child in soup.p.descendants:
#     print(child)
print(soup.find_all('a'))
print(len(soup.find_all('a')))
for a in soup.find_all('a'):
    print(a.find_all('span'))
    print(a.string)
print(soup.find_all(attrs={'class': 'sister'}))
print(soup.find_all(class_ = 'sister'))  # 和上面一样
print(soup.find_all(id='link3'))
