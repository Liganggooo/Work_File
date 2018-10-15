import requests
import re
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import pymysql
db = pymysql.connect('localhost','root','lg083533','student')
cursor = db.cursor()
def get_one_page(url):
	try:
		content = requests.get(url)
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None
	

def parser_one_movie(html):
	soup = BeautifulSoup(html,'html.parser')
	results = soup.select(".item")
	#提取电影名
	for result in results:
		title = result.select('.nbg')[0]
		# print(title['title'])
		# #提取演员
		actor = result.select('.pl')[0].get_text()
		# # # print('演员：' + actor)
		# # #根据span标签提出span相关的内容
		comment = result.select('.pl')[1].get_text()
		comment = int(re.compile('(\d+)').search(comment).group(1))
		# print(comment)
		rating_nums = result.select('.rating_nums')[0].get_text()
		rating_nums = float(rating_nums)
		# print('豆瓣评分：' + rating_nums)
		# print(result)
		# movies = {
		# 	'电影': title['title'],
		# 	# '演员': actor,
		# 	'评论人数': comment,
		# 	'豆瓣评分': float(rating_nums)
		# }
		saveToSQL(title['title'],comment,rating_nums)
#创建一个数据库表格
def CreateSql():
	try:
		cursor.execute('drop table if exists DoubanMovies')
		sql = 'create table DoubanMovies\
	(电影 char(20),评论数 char(10),豆瓣评分 char(10))' 
		cursor.execute(sql)
	except Exception as ex:
		print(ex)

def saveToSQL(movieName,comment,rateNum):
	sql = 'insert into DoubanMovies values (%s,%s,%s)'
	try:
		cursor.execute(sql,(movieName,comment,rateNum))
		db.commit()

	except Exception as ex:
		db.rollback()
		print(ex)




def main():
	url = 'https://movie.douban.com/chart'
	CreateSql()
	html = get_one_page(url)
	res = parser_one_movie(html)

if __name__ == '__main__':
	main()





