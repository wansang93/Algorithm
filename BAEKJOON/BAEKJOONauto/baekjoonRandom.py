# 백준 로또 맞을 때 까지 돌리는 프로그램

import pickle
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\wansang\chromedriver.exe")

options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

### 사람처럼 보이게 하는 옵션들 ###
# 가속 사용 x
options.add_argument("disable-gpu")
# 가짜 플러그인 탑재
options.add_argument("lang=ko_KR")
# user-agent 이름 설정
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

url = 'https://www.acmicpc.net/login'

driver.get(url)

driver.find_element_by_name('login_user_id').send_keys('')
driver.find_element_by_name('login_password').send_keys('')
driver.implicitly_wait(5)
driver.find_element_by_id('submit_button').click()
print(driver.get_cookies())

# 쿠키 저장
pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

# 쿠키 불러오기
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)






while True:
    pass