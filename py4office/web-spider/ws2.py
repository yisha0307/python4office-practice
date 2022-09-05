# 爬虫示例
from urllib import parse
from urllib import request

url = 'https://www.baidu.com/s?wd={}'
# 想要搜索的内容
word = input('请输入搜索内容: ')
params = parse.quote(word)
full_url = url.format(params)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
# 创建请求对象
req = request.Request(url=full_url, headers=headers)
# 获取相应对象
res = request.urlopen(req)
html = res.read().decode('utf-8')

# 保存为本地文件
filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
