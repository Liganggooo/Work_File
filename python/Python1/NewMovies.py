import requests
import re
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import pymongo
from config import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_one_page(url):
	try:
		content = requests.get(url)
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None
	

def parser_one_movie(html,num):
	soup = BeautifulSoup(html,'html.parser')
	result = soup.select(".item")[num]
	#提取电影名
	title = result.select('.nbg')[0]
	# print(title['title'])
	#提取演员
	actor = result.select('.pl')[0].get_text()
	# print('演员：' + actor)
	#根据span标签提出span相关的内容
	comment = result.select('span')[3].get_text()
	# print("评价人数：" + comment)
	rating_nums = result.select('.rating_nums')[0].get_text()
	# print('豆瓣评分：' + rating_nums)
	# print(result)
	return {
		'电影': title['title'],
		'演员': actor,
		'评论人数': comment,
		'豆瓣评分': rating_nums
	}


# def write_to_file(res):
# 	with open("New_movies.txt",'a',encoding = 'utf-8') as f:
# 		f.write(json.dumps(res,ensure_ascii = False) + '\n')
# 		f.close
def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
			print('存储到MongoDB成功..',result)
	except Exception:
		print('存储到MongoDB成功..',result)




def main():
	url = 'https://movie.douban.com/chart'
	html = get_one_page(url)
	for i in range(9):
		res = parser_one_movie(html,i)
		# print(res)
		# write_to_file(res)
		save_to_mongo(res)


if __name__ == '__main__':
	main()
