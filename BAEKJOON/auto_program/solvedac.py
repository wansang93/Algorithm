"""
Version 0.01
solved ac 브론즈 문제 크롤링 기본
"""

import requests
from bs4 import BeautifulSoup

LINK = 'https://solved.ac/problems/level/2'
LINK2 = 'https://solved.ac/problems/level/2?page=2'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

htmls = requests.get(LINK, headers=headers)
bs = BeautifulSoup(htmls.content, 'html.parser')

solved_list = []
for table in bs.select('.gnrMGL'):
    temp = []
    number = table.select('div:first-child')[0].text
    temp.append(number)
    for title in table.select('div:nth-child(2)'):
        temp.append(title.text)
    solved_list.append(temp)

for row in solved_list:
    print(*row)
