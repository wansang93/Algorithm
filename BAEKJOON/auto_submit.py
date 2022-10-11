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

import time
from selenium import webdriver

PROBLEM_NUMBER = 10944
URL_10944_SUBMIT = f"https://www.acmicpc.net/submit/{PROBLEM_NUMBER}/44444443"

driver = webdriver.Chrome()

# TODO: 1-1. 로그인 한번 하기(세션 생성)

# TODO: 1-2. 로그인 쿠키 저장
driver.add_cookie()

while True:
    # 2. 5초 계산 프로그램
    time.sleep(5)
    break

    # TODO: 문제 정답인지 확인

    # 문제 들어가기(풀이 포함)
    driver.get(URL_10944_SUBMIT)

    # 문제 제출하기
    driver.find_element('submit_button').click()
