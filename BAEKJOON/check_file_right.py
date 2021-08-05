'''
이 파일은 내가 푼 문제 모두가 README.md의 리스트에 잘 들어갔는지 체크하는 문서입니다.

Ver0.01(21-02-01)

1. 백준 정답을 복사하여 체크한다.
2. 파일 목록을 체크한다.
3. readme.md 목록을 복사하여 체크한다.

1, 2, 3번의 3가지를 비교하여 없거나 추가한 것을 체크한다.
비교된 것을 수동으로 바꿔준다.

Ver0.02(21-07-06)

1. 백준에서 내가 푼 문제를 크롤링해서 자동으로 따오기 -> list
2. 파일 목록을 자동으로 체크하기 -> list
    2-1. 백준 목록과 파일 목록 비교 후 파일 없는 것 확인하기
3. README.md파일을 탐색하면서 파일 목록에 없는 것 추가하기 -> 쓰기
'''

import re
import os

import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈


# 1. Check how many solved problems in BAEKJOON
USER_NAME = 'wansang93'
solved_BAEKJOON_list = []

link = 'https://www.acmicpc.net/user/' + USER_NAME
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
baekjoon_lst = soup.find('div', class_='panel-body')

for atag in baekjoon_lst:
    string = atag.string
    if string.isdecimal():
        solved_BAEKJOON_list.append(int(string))

# print(solved_BAEKJOON_list, len(solved_BAEKJOON_list))


# 2. Check how many solved problems files are in my folder
TARGET_DIR = r"C:/Users/wansang/Desktop/Gitrep/Algorithm/BAEKJOON/problems"
all_file_list = os.listdir(TARGET_DIR)

my_files_list = []
for file in all_file_list:
    file_name, extension = file.rsplit('.')
    if file_name.isdecimal():
        my_files_list.append(int(file_name))

my_files_list.sort()
# print(my_files_list, len(my_files_list))

# 2-1. 백준 파일과 나의 파일 목록 확인하기
none_files_list = list(set(solved_BAEKJOON_list) - set(my_files_list))
none_baek_list = list(set(my_files_list) - set(solved_BAEKJOON_list))
print(' 백준 의 파일:', len(solved_BAEKJOON_list))
print('내폴더의 파일:', len(my_files_list))
print('내폴더에 없는 파일:', none_files_list)
print('내폴더에 없는 파일:', none_baek_list)


# 3. TODO: md 파일에 번호 순서대로 문제 넣기
MD_FILE = r'C:/Users/wansang/Desktop/Gitrep/Algorithm/BAEKJOON/README.md'

# TODO: 나중에 수정하기
file_not_in_mdlist = []
with open(MD_FILE, 'r', encoding='utf-8') as f:
    pass

none_files_list = []
with open(MD_FILE, 'a', encoding='utf-8') as f:
    for i in solved_BAEKJOON_list:
        # f.writelines(f'- [{i}](./problems/{i}.md)\n')
        pass
