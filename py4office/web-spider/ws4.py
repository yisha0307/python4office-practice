from urllib import parse, request
import time
import random
from ua_info import ua_list  # 定义ua池

# 定义一个爬虫类
class TiebaSpider():
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?{}'

    # 请求函数：得到页面
    def get_html(self, url):
        req = request.Request(url = url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html
    
    # 解析函数
    # 暂时空着
    def parse():
        pass

    # 3、保存文件函数
    def save_html(self, file_name, html):
        with open(file_name, 'w') as f:
            f.write(html)
    
    # 入口函数
    def run(self):
        name = input('请输入贴吧名: ')
        begin = int(input('请输入起始页：'))
        end = int(input('请输入终止页: '))

        for page in range(begin, end):
            pn = (page-1)*50
            params = {
                'kw': name,
                pn: pn
            }
            params = parse.urlencode(params)
            url = self.url.format(params)
            # 发请求
            html = self.get_html(url)
            # 定义路径
            filename = '{}-{}页.html'.format(name, page)
            self.save_html(filename, html)

            print('第%d页抓取成功'%page)
            # 每抓取一个页面后休眠1-2秒钟
            time.sleep(random.randint(1,2))

# 以脚本的形式运行爬虫
if __name__ == '__main__':
    start = time.time()
    spider = TiebaSpider()  #实例化一个webspider对象
    spider.run()
    end = time.time()
    print('执行时间: %.2f秒'%(end-start))  # 查看运行时间
    



