from __future__ import unicode_literals
from wxpy import *
from threading import Timer
import requests
from bs4 import BeautifulSoup
import time
bot = Bot()

friend = bot.friends()

# print(friend)
def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parsePage(html):
    soup = BeautifulSoup(html,'html.parser')
    contents = soup.select('.main')[0].select('.sort_list')
    for content in contents:
        EnText = content.select('.c_l_m_en')[0].select('a')[0].get_text()
        ZhText = content.select('.c_l_m_cn')[0].select('a')[0].get_text()
        # print(EnText,ZhText)
        send_msg(EnText,ZhText)
        time.sleep(30)

def send_msg(massage1,massage2):
    try:
        myfriend = friend.search(u'大兵')[0]
        myfriend.send(massage1)
        myfriend.send(massage2)
        myfriend.send(u'来自宝宝的心灵鸡汤！')

    except:
        myfriend = friend.search(u'老夫气鼓鼓')[0]
        myfriend.send(u'信息发送失败！')

def main(offset):
    url = 'http://news.iciba.com/appv3/wwwroot/ds.php?action=history&ob=1&order=2&page= ' + str(offset)
    html = get_page(url)
    parsePage(html)
    # send_msg()

if __name__ == '__main__':
    for i in range(1,301):
        main(i)








