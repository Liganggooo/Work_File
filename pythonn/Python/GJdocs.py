import requests
from pyquery import PyQuery as pq
import json
def parseIndex(url):
	try:
		content = requests.get(url)
		content.encoding = 'utf-8'
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None

def getLink(html):
	doc = pq(html)
	items = doc('.right-list .right-list-box ul li')
	links = []
	for item in items.items():
		# print(type(item))
		link = item.find('a').attr('href')
		links.append(link)
	return links

def getDetail(link):
	try:
		response = requests.get(link)
		response.encoding = 'utf-8'
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parseDoc(html):
    doc = pq(html)
    items = doc('.article #Zoom .zw-con')
    for item in items.items():
        title = doc('.article .Article_bt')
        title = title.find('h1').text()
        content = item.find('p').text()
        passage = {
        	'标题': title,
        	'正文': content
        }
        # print('公文标题：',title)
        # print('公文正文：',content)
        saveToMongo(passage)

def saveToMongo(passage):
	with open('doc.json','a',encoding = 'utf-8') as f:
		f.write(json.dumps(passage,ensure_ascii = False) + '\n')
		f.close

def main(num):
	url = 'http://www.gzgov.gov.cn/xxgk/jbxxgk/fgwj/gjflfgjgz/index_{}.html'.format(num)
	html = parseIndex(url)
	links = getLink(html)
	# print(links)
	for link in links:
		result = getDetail(link)
		parseDoc(result)
		# print(passage)


if __name__ == '__main__':
	for i in range(1,33):
		main(i)























