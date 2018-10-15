# def test():
# 	a = 100
# 	def test2():
# 		print(a)
# 		#a = 120
# 	return test2
# result = test()
# result()


# import requests
# newurl = 'http://news.sina.com.cn/ruijian/'
# res = requests.get(newurl)
# res.encoding = 'utf-8'
# print(res.text)


# import requests
# from bs4 import BeautifulSoup
# newurl = 'http://widget.weibo.com/relationship/\
# followbutton.php?btn=light&style=1&uid=2288776865\
# &width=68&height=22&language=zh_cn'
# res = requests.get(newurl)
# res.encoding = 'unicode' 
# soup = BeautifulSoup(res.text,'html.parser')


from bs4 import BeautifulSoup
html_sample = ' \
<html> \
 <body> \
 <h1 id="title">Hello World</h1> \
 <a href="#" class="link">This is link1</a> \
 <a href="# link2" class="link">This is link2</a> \
 <a target="_blank" class="linkto" href="http://new.qq.com/omn/NEW2018042200486400">蓝图绘就梦想——《河北雄安新区规划纲要》发布</a>\
 </body> \
 </html>'
soup = BeautifulSoup(html_sample,'html.parser')
# print(type(soup))
# print(soup.text)

# tit = soup.select('h1')
# titl = soup.select('#title')
# print(tit[0])
# print(titl[0])

alink = soup.select('a')[0].get_text()
print(alink)

# for link in soup.select('.link'):
#     print(link)
#     print(link['href'])
#     print(link.text)
# linktoo = soup.select('.linkto')
# print(linktoo)