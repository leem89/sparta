import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td > a.title.ellipsis')
for index, music in enumerate(musics):
    title = music.get_text().strip()
    print(str(index + 1) + '.', title)

#<score를 따로 빼서 해결하려고 했지만 실패....
# import requests
# from bs4 import BeautifulSoup

# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbsparta

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# for music in musics:
#     titles = music.select_one('td > a.title.ellipsis')
#     scores = music.select_one('td.number')
#     if titles is not None:
#         title = titles.get_text().strip()
#         score = scores.get_text().strip()
#         print(score)
# 망한코드.......