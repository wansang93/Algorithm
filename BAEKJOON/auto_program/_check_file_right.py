'''
이 파일은 제가 푼 문제 모두가 README.md의 리스트에 잘 들어갔는지 체크하는 문서입니다.

#################### Ver0.01(21-02-01) ####################

1. 백준 정답을 복사하여 체크한다.
2. 파일 목록을 체크한다.
3. readme.md 목록을 복사하여 체크한다.

1, 2, 3번의 3가지를 비교하여 없거나 추가한 것을 체크한다.
비교된 것을 수동으로 바꿔준다.

#################### Ver0.02(21-07-06) ####################

1. 백준에서 내가 푼 문제를 크롤링해서 자동으로 가져오기
2. 파일 목록을 자동으로 체크하기
    2-1. 백준 목록과 파일 목록 비교 후 파일 없는 것 확인하기
3. README.md 파일을 탐색하면서 파일 목록에 없는 것 추가하기

#################### Ver0.03(22-01-26) ####################

1. 함수화
2. 웹 페이지 변경으로 인한 크롤링 방식 변경
'''

import os
import requests
from bs4 import BeautifulSoup

# 링크 정보
USER_NAME = 'wansang93'
LINK = 'https://www.acmicpc.net/user/' + USER_NAME
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# 리스트 전역변수
solved_baekjoon_list = []
my_files_list = []

# 폴더 링크
TARGET_DIR = r"C:/Users/wansang/Desktop/Gitrep/Algorithm/BAEKJOON/problems"
MD_FILE = r'C:/Users/wansang/Desktop/Gitrep/Algorithm/BAEKJOON/README.md'


# 1. Check how many solved problems in BAEKJOON
def count_solved_in_BAEKJOON():
    response = requests.get(LINK, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    baekjoon_lst = soup.find('div', class_='problem-list')
    for atag in baekjoon_lst:
        # print(atag)
        string = atag.string
        if string.isdecimal():
            solved_baekjoon_list.append(int(string))

    # print(solved_BAEKJOON_list, "갯수:", len(solved_BAEKJOON_list))


# 2. Check how many solved problems files are in my folder
def count_files_in_my_folder():
    all_file_list = os.listdir(TARGET_DIR)

    for file in all_file_list:
        file_name, extension = file.rsplit('.')
        if file_name.isdecimal():
            my_files_list.append(int(file_name))

    my_files_list.sort()
    # print(my_files_list, len(my_files_list))


# 2-1. 백준 파일과 나의 파일 목록 확인하기
def check_what_is_diff():
    none_files_list = sorted(set(solved_baekjoon_list) - set(my_files_list))
    none_baek_list = sorted(set(my_files_list) - set(solved_baekjoon_list))
    print(f'  백준의 파일 갯수: {len(solved_baekjoon_list):04,d}개')
    print(f'내폴더의 파일 갯수: {len(my_files_list):04,d}개')
    print(f'  백준에 없는 파일: {len(none_baek_list):04,d}개', none_baek_list)
    print(f'내폴더에 없는 파일: {len(none_files_list):04,d}개', none_files_list)


# 3. TODO: 삭제 후 지우기가 아닌 덮어쓰기 형식으로 변경하기
def write_on_md_file():
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        lst_of_lines = f.readlines()
        template = lst_of_lines[:19]

    with open(MD_FILE, 'w', encoding='utf-8') as f:
        f.writelines(template)
        for i, v in enumerate(solved_baekjoon_list, 1):
            if 1000 <= v < 10000:
                f.writelines(f'&nbsp;&nbsp;&nbsp;[{v}](./problems/{v}.md)')
            else:
                f.writelines(f'&nbsp;[{v}](./problems/{v}.md)')
            if i % 10 == 0:
                f.writelines(f'\n\n')
        f.writelines('\n')


if __name__ == "__main__":
    count_solved_in_BAEKJOON()
    count_files_in_my_folder()
    check_what_is_diff()
    write_on_md_file()
