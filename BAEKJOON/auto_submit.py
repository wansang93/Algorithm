"""
==================== Alpha 0.01 ====================
프로그램 설명: 
랜덤게임 자동 제출 프로그램 입니다.
10944번을 참고 예시로로 만들었습니다.
"""

"""
__summary__
__진행중__
설계
1. 첫 로그인, 로그인 후 쿠키 세션으로 로그인
2. 5초(계산 필요) 웨이팅
3. 문제 맞춘지 확인
    - 맞추면 프로그램 종료
3. 문제 번호 제출로 이동
    - 문제 풀이 입력
    - 제출
    - 2번 루프로 이동
"""


# import requests
# from bs4 import BeautifulSoup as bs

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# LOGIN_INFO = {"login_user_id":"wansang93", "login_password":""}
# boj_url = "https://www.acmicpc.net/signin"

# with requests.Session() as sess:
#     sess.post(boj_url, data=LOGIN_INFO)
#     soup = bs(sess.get(boj_url).text, 'html.parser')
#     print(soup)
#     if soup.find('a', {'class': 'username'}) is None:
#         print("Invalid login info")
#     else:
#         print(soup.find('a', {'class': 'username'}))

import time
from selenium import webdriver

def selenium():
    BOJ_URL = "https://www.acmicpc.net"
    ACTION = "submit"
    PROBLEM_NUMBER = 10944
    SUBMIT_NUMBER = 44444443
    DO_URL = f"{BOJ_URL}/{ACTION}/{PROBLEM_NUMBER}/{SUBMIT_NUMBER}"

    driver = webdriver.Chrome()

    # TODO: 1-1. 로그인 한번 하기(세션 생성)

    # TODO: 1-2. 로그인 쿠키 저장
    while True:
        # 2. 5초 계산 프로그램
        driver.get(DO_URL)
        time.sleep(15)
        driver.get("https://www.acmicpc.net/submit/10944/44444443")
        time.sleep(4)
        # TODO: 문제 정답인지 확인

        # 문제 들어가기(풀이 포함)

        # 문제 제출하기
        driver.find_element(by=id, value='submit_button').click()

if __name__ == "__main__":
    selenium()
