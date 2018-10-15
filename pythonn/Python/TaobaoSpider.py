from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re
from pyquery import PyQuery as pq
from config import *
import pymongo
brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def search():
	try:
		brower.get('https://www.taobao.com/')
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
		submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
		input.send_keys('美食')
		submit.click()
		page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
		# input.clear()
		# input.send_keys(Keys.RETURN)
		return page.text
	except TimeoutException:
		return search()
def next_page(page_num):
	try:
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
		input.clear()
		input.send_keys(page_num)
		input.send_keys(Keys.RETURN)
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active"),str(page_num)))
		parse_page()
	except TimeoutException:
		return next_page()

def parse_page():
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))
	html = brower.page_source
	doc = pq(html)
	items = doc('#mainsrp-itemlist .items .item').items()
	count = 0
	for item in items:
		product = {
			# 'image':item.find('.pic .img').attr('stc'),
			'price':item.find('.price').text(),
			'deal':item.find('.deal-cnt').text()[0:-3],
			'title':item.find('.title').text(),
			'shop':item.find('.shopname').text(),
			'location':item.find('.location').text()
		}
		count +=1
		# print(product)
		# save_to_mongo(product)
	print(count)

def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
			print('存储到MongoDB成功..')
	except Exception:
		print('存储到MongoDB成功..')

def main():
	try:
		page = search()
		page = int(re.compile('(\d+)').search(page).group(1))
		for i in range(1,page+1):
			next_page(i)

		time.sleep(5)
	except Exception:
		print('出错了..')
	finally:
		brower.quit()

if __name__ == '__main__':
	main()













