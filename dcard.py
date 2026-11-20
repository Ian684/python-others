# import requests
# from bs4 import BeautifulSoup
# import json
# quotes = []
# for page in range(1,6):
#     url = f'https://quotes.toscrape.com/page/{page}/'
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text ,'html.parser')
#     quotes.append({'page':page})
#     for quote in soup.select('.quote'):
#         text = quote.select_one('.text').text
#         author = quote.select_one('.author').text
#         quotes.append({'text':text,'author':author})
# with open('yeeee.json','w',encoding='utf-8') as file:
#     json.dump(quotes,file,ensure_ascii=False,indent=2)

# import requests
# from bs4 import BeautifulSoup
# import json
# url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
# res = requests.get(url)
# data = res.json()
# station = []
# for i ,j in data['retVal'].items():
#     station.append({'站點': j['sna'],
#         '地址': j['ar'],
#         '可借車輛': int(j['sbi']),
#         '可停空位': int(j['bemp'])})
# with open('station.json' ,'w' ,encoding='utf-8') as file:
#     json.dump(station ,file ,ensure_ascii=False ,indent=2)

import requests
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime
import time

logging.basicConfig(filename='dcard.log' ,level=logging.INFO ,format='%(asctime)s - %(levelname)s - %(message)s')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dcard.tw/',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Mobile': '?0'
}
url = 'https://www.dcard.tw/service/api/v2/posts?popular=true&limit=30'
def dcard_hot(save):
    logging.info('start document')
    documents = fetch(url ,headers)
    if documents is None:
        logging.warning('no fetch')
        return
    parsed_documents = [parse(p) for p in documents]
    date_str = datetime.now().strftime('%Y%m%d')
    if save == 'csv':
        to_csv(parsed_documents ,f'dcard_hot_{date_str}.csv')
    elif save == 'json':
        to_json(parsed_documents ,f'dcard_hot_{date_str}.json')
    else:
        logging.warning('format failed')
        return
    logging.info('completed')
def fetch(url ,headers):
    try:
        res = requests.get(url ,headers=headers ,timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        logging.error(f'failed{e}')
        return[]
def parse(document):
    return{
         'id': document.get('id'),
        'title': document.get('title'),
        'excerpt': document.get('excerpt'),
        'likeCount': document.get('likeCount'),
        'commentCount': document.get('commentCount'),
        'createdAt': document.get('createdAt'),
        'forumName': document.get('forumName'),
        'gender': document.get('gender'),
        'school': document.get('school'),
        'url': f"https://www.dcard.tw/f/{document.get('forumAlias')}/p/{document.get('id')}"
    }
def to_csv(parsed_documents ,file):
    try:
        with open(file ,'w' ,encoding='utf-8') as f:
            heads = list(parsed_documents[0].keys())
            f.write(','.join(heads) + '\n')
            for line in  parsed_documents:
                values = [str(line.get(h,'')) for h in heads]
                values = [v.replace('\n' ,'').replace(',' ,'，') for v in values]
                f.write(','.join(values) + '\n')
    except Exception as e:
        logging.error(f'error:{e}')
def to_json(parsed_documents ,file):
    try:
        with open(file ,'w' ,encoding='utf-8') as f:
            json.dump(parsed_documents ,f ,ensure_ascii=False ,indent=2)
        logging.info(f'success in {file}')
    except Exception as e:
        logging.error(f'error:{e}')
if __name__ == '__main__':
    dcard_hot('csv')
