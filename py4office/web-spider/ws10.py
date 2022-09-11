# 爬取b站的弹幕
import requests
from bs4 import BeautifulSoup
from ua_info import ua_list
import random

class Danmu():
    def __init__(self):
        self.url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=825906632'
        self.headers = {
            'user-agent': random.choice(ua_list)
        }
    
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html

    def parse_html(self):
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        list = soup.select('i d')
        with open('danmu.txt', 'w') as f:
            for dd in list:
                f.write(dd.string)
                f.write('\n')

if __name__== '__main__':
    danmu = Danmu()
    danmu.parse_html()
        
