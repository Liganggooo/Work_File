import requests
import re
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
def get_one_page(url):
	try:
		content = requests.get(url)
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None	

def parser_one_movie(html):
	# pattern = re.compile('<a\sclass="nbg".*?title="(.*?)".*?</a>',re.S)
	pattern = re.compile('<a\sclass="nbg"\shref="(.*?)".*?\
title="(.*?)".*?</a>.*?font-size:13px;">(.*?)</span>',re.S)
	items = re.findall(pattern,html)
	# print(items)
	res = []
	for item in items:
		res.append(item[0])		
	return res	

def get_page_detail(detail_url):
	try:
		respone = requests.get(detail_url)
		if respone.status_code == 200:
			return respone.text
		return None
	except RequestException:
		return None

def parser_page_detail(detail_html):
	soup = BeautifulSoup(detail_html,'html.parser')
	title = soup.select('#content')[0]
	title = title.select('h1')[0]('span')
	content_html = soup.select('#link-report')[0]
	content = content_html('span')[0]
	# print(title[0].text,title[1].text)
	# print(content.text.strip())
	return {
		'电影名':title[0].text + '' + title[1].text,
		'电影简介':content.text.strip()
	}
def write_to_file(resu):
	with open('Movie.txt','a',encoding = 'utf-8') as f:
		f.write(json.dumps(resu,ensure_ascii = False) + "\n")

def main():
	url = 'https://movie.douban.com/chart'
	html = get_one_page(url)
	results = parser_one_movie(html)
	for result in results:
		detail_html = get_page_detail(result)
		resu = parser_page_detail(detail_html)
		print('电影加载中...')
		print(resu)
		# write_to_file(resu)


if __name__ == '__main__':
	main()




