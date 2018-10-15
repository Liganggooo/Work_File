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
	

def parser_one_anchor(html,num):
	soup = BeautifulSoup(html,'html.parser')
	#获得直播标题
	title = soup.select('.play-list-link')[num]
	# print(title)
	# print('标题：',title['title'])

	#获得直播类型
	tag = title.select('.mes-tit')[0]
	tag = tag.select('span')[0]
	# print('直播类型：',tag.text)
	#获得主播名称
	name = title.select('.mes')[0]('span')[1]
	# print('主播名：',name.text)
	#获取主播人气
	enrages = title.select('.mes')[0]('span')[2]
	# print('人气：',enrages.text)
	#获取主播个人标签
	Mantra = title.select('.impress-tag-list')[0]
	# print('主播个人标签：',Mantra.text)
	return {
		'标题': title['title'],
		'直播类型': tag.text,
		'主播名': name.text,
		'人气': enrages.text,
		'主播个人标签': Mantra.text
	}

def write_to_file(res):
	with open("DouyuAnchor.json",'a',encoding = 'utf-8') as f:
		f.write(json.dumps(dict(res),ensure_ascii = False) + '\n')
		f.close

def main():
	url = 'https://www.douyu.com/directory/game/LOL'
	html = get_one_page(url)
	for i in range(120):
		print(i+1)
		result = parser_one_anchor(html,i)
		print(result)
		write_to_file(result)


if __name__ == '__main__':
	main()






