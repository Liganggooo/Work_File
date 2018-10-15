# def test():
# 	a = 100
# 	def test2():
# 		print(a)
# 		#a = 120
# 	return test2
# result = test()
# result()


# import requests
# newurl = 'http://news.qq.com/'
# res = requests.get(newurl)
# print(res.text)


# import requests
# from bs4 import BeautifulSoup
# newurl = 'newurl = 'http://news.qq.com/'
# res = requests.get(newurl)
# res.encoding = 'unicode' 
# soup = BeautifulSoup(res.text,'html.parser')


# from bs4 import BeautifulSoup
# html_sample = ' \
# <html> \
#  <body> \
#  <h1 id="title">Hello World</h1> \
#  <a href="#" class="link">This is link1</a> \
#  <a href="# link2" class="link">This is link2</a> \
#  <a target="_blank" class="linkto" href="http://new.qq.com/omn/NEW2018042200486400">蓝图绘就梦想——《河北雄安新区规划纲要》发布</a>\
#  </body> \
#  </html>'
# soup = BeautifulSoup(html_sample,'html.parser')
# print(type(soup))
# print(soup.text)

# tit = soup.select('h1')
# titl = soup.select('#title')
# print(tit[0])
# print(titl[0])

# alink = soup.select('a')
# print(alink[0])

# for link in soup.select('.link'):
#     print(link)
#     print(link['href'])
#     print(link.text)
# linktoo = soup.select('.linkto')
# print(linktoo)




#制作第一只腾讯新闻爬虫
# import requests
# from bs4 import BeautifulSoup
# newurl = 'http://news.qq.com/'
# res = requests.get(newurl)
# print(type(res))
# soup = BeautifulSoup(res.text,'html.parser')
# print(res.text)

#提取新闻标题与链接
# import requests
# from bs4 import BeautifulSoup
# newurl = 'http://news.qq.com/'
# res = requests.get(newurl)
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.text)


#计算新闻的个数
# count = 0
# news_text_text , news_text_url = [] , []
# for news in soup.select('.text'):
# 	count += 1
# 	try:
# 		news_text = news.select('a')[0].text
# 		alink = news.select('a')[0]['href']
	# except IndexError:
		# pass
	# else:
		# print(news_text,alink)
		# news_text_url['text'] = news_text
		# news_text_url['url'] = alink
		# news_text_text.append(news_text)
		# news_text_url.append(alink)

#将标题和链接分别存入列表中并遍历，卵用都没有
# for n in news_text_url:
	# print(n)
# print(news_text_url['url'])

# print(count)
# 抓去文章内文
# import requests
# from bs4 import BeautifulSoup
# newsurl = 'http://new.qq.com/omn/FIN2018042200709000'
# resq = requests.get(newsurl)
# soup = BeautifulSoup(resq.text,'html.parser')
# print(resq.text)
# print(soup.select('.one-p'))


