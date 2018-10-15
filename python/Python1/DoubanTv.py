import requests
from requests.exceptions import RequestException
import re
import json
from bs4 import BeautifulSoup
def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parser_one_page(html):
	soup = BeautifulSoup(html,'html.parser')
	# print(soup.text)
	#json 类文件提取方法
	js = json.loads(soup.text)
	return js['subjects']
		

def write_to_file(content):
	with open('DoubanTv.txt','a',encoding = 'utf-8') as f:
		f.write(json.dumps(content,ensure_ascii = False) + '\n')
		f.close()

def main(start):
	url = 'https://movie.douban.com/j/\
search_subjects?type=tv&tag=\
%E7%83%AD%E9%97%A8&sort=\
rank&page_limit=20&page_start=' + str(start)
	html = get_one_page(url)
	for res in parser_one_page(html):
		write_to_file(res)
		print(res)


if __name__ == '__main__':
	for i in range(26):
		main(i*20)









