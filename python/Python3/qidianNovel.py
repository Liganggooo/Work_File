from lxml import etree
import requests
from requests.exceptions import RequestException
import json
import pymongo
from config import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_index(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None
def parser_index(html):
	content = etree.HTML(html)
	links = content.xpath('//*[@class="book-img-text"]//li')
	link_list = []
	for link in links:
		href = link.xpath('./div[2]/h4/a/@href')[0]
		link_list.append(href)
	return link_list

def get_detail(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parser_detail(html):
	content = etree.HTML(html)
	novel_name = content.xpath('/html/body/div[2]/div[6]/div[1]//h1/em/text()')[0]
	author = content.xpath('/html/body/div[2]/div[6]/div[1]//h1/span/a/text()')[0]
	monthCount = content.xpath('//*[@id="monthCount"]/text()')[0]
	return {
		'novel_name': novel_name,
		'author': author,
		'monthCount': monthCount
	}

# def write_to_file(result):
# 	with open('novel_rank.json','a',encoding = 'utf-8') as f:
# 		f.write(json.dumps(result,ensure_ascii = False) + '\n')
# 		f.close

def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
			print('存储到到MongoDB成功...',result)
	except Exception:
		print('存储到MongoDB失败...',result)

		

def main(page):
	url = 'https://www.qidian.com/rank/yuepiao?style=1&page=' + str(page)
	html = get_index(url)
	link_list = parser_index(html)
	for link in link_list:
		detail_html = get_detail('https:' + link)
		result = parser_detail(detail_html)
		# write_to_file(result)
		# print(result)
		save_to_mongo(result)



if __name__ =='__main__':
	for i in range(1,26):
		main(i)





















