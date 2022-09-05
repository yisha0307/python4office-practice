# urllib：内置的获取html的库
import urllib.request

res = urllib.request.urlopen('http://www.baidu.com/')
print(res)

html = res.read().decode('utf-8')  # decode()转换成字符串
# print(html)
url = res.geturl()
print(url)
code = res.getcode()
print(code)

response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()  # user-agent: Python-urllib/3.8
print(html)

# 重构爬虫UA信息
url = 'http://httpbin.org/get'
headers = {
    # 伪装成chrome浏览器
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')  #user-agent被改了
print(html)