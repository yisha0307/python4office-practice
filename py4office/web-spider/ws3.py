# 爬虫示例
# 函数式编程
from fileinput import filename
from urllib import parse
from urllib import request

# 拼接url地址
def get_url(word):
    url = 'https://www.baidu.com/s?{}'
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url

# 发请求，保存本地文件
def request_url(url, filename):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

# 主程序入口
if __name__ == '__main__':
    word = input('请输入搜索内容: ')
    url = get_url(word)
    filename = word + '.html'    
    request_url(url, filename)