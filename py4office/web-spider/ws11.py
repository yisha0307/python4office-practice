# 抓取新京报的标题
from urllib import response
import requests
from ua_info import ua_list
from bs4 import BeautifulSoup
import random

class Title():
    def __init__(self):
        self.url = 'https://www.bjnews.com.cn/search?bwsk=%E4%BA%BA%E5%8F%A3'
        self.headers = {
            'user-agent': random.choice(ua_list)
        }
    
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html

    def recode(self):
        html = self.get_html()
        print(html)
        soup = BeautifulSoup(html, 'lxml')
        title_list = soup.select('.articleTitle')
        print(title_list)
        # list_string = [x.string for x in title_list]
        # with open('xinjingbao.txt', 'w') as f:
        #     for t in list_string:
        #         f.write(t)
        #         f.write('\n')

if __name__=='__main__':
    title = Title()
    title.recode()