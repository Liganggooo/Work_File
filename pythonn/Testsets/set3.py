import requests
import re
import csv
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_index(url):
    try:
        content = requests.get(url)
        if content.status_code == 200:
            return content.text
        return None
    except RequestException:
        return None


def parse_region(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    region = soup.select('.mp-sidebar-list')[0]
    hotcitys = region.select('li')
    link_list = []
    for hotcity in hotcitys:
        city = hotcity.get_text().strip()
        link = url + hotcity.select('a')[0]['href']
        link_list.append(link)
    #         print(city)
    return link_list


def parse_sight(html):
    soup = BeautifulSoup(html, 'html.parser')
    result_list = soup.select('.result_list')[0]
    sight_item = result_list.select('.sight_item')
    sight_list = []
    for item in sight_item:
        name = item.select('.sight_item_caption')[0].get_text()
        info = item.select('.sight_item_info')[0]
        #         level = info.select('.level')[0].get_text()
        area = info.select('.area')[0].get_text().replace('[', '').replace(']', '')
        hot = info.select('.product_star_level')[0].get_text()
        hot_num = re.compile('(\d+\.\d)').search(hot).group(1)
        sale = item.select('.sight_item_pop')[0].select('.hot_num')[0].get_text()
        #         print(level)
        list = [name, area, hot_num, sale]
        print(list)
        sight_list.append(list)
    return sight_list


def write_to_csv(itemlist):
    with open('GuiZhou.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['景区', '地址', '热度', '销量'])
        for item in itemlist:
            # print(item)
            writer.writerow(item)


def main(i):
    url = 'http://piao.qunar.com/'
    html1 = get_index(url)
    link_list = parse_region(html1, url)
    link = 'http://piao.qunar.com/ticket/list.htm?keyword=贵州&region=贵州&from=mpl_search_suggest&page= ' + str(i)
    html2 = get_index(link)
    list = parse_sight(html2)
    write_to_csv(list)


if __name__ == '__main__':
    for i in range(1, 11):
        main(i)
