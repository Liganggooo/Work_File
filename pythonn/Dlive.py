import json
import requests
import pymongo
from requests.exceptions import RequestException
from config import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_json_index(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None


# print(html)
def parse_page(response):
    html = response.content.decode()
    content = json.loads(html)
    infos = content['data']['rl']
    for info in infos:
        title = info['rn']
        name = info['nn']
        enrages = info['ol']
        tags = info['c2name']
    # print(title,name,enrages,tags)
        result = {
            '标题': title,
            '主播名': name,
            '人气': enrages,
            '标签': tags
        }
        # save_to_mongo(result)
# pass
def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("存储到MONGODB成功..")
    except Exception:
        print("存储到MONGODB失败..")


def main(offset):
    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/' + str(offset)
    response = get_json_index(url)
    parse_page(response)

if __name__ == '__main__':
    for i in range(1, 78):
        main(i)

















