# import requests
# from bs4 import BeautifulSoup

# res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
# soup = BeautifulSoup(res.content, 'html.parser')

# section = soup.find("ul", id='dev_course_list')
# titles = section.find_all('li', 'course')
# for index, title in enumerate(titles):
#     # print(type(title.get_text()))
#     print(str(index+1) + '.', title.get_text().split('[')[0].split('-')[1].strip())

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('#harmonyContainer')

for item in items:
    print (item.get_text())