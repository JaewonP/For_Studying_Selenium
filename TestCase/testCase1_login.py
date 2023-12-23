from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 
# selenium webdriver 에서 크롬 브라우저 지원 중
driver.get('http://www.naver.com')

# 네이버 로그인 로고 클릭
search_logo = driver.find_element(By.CLASS_NAME, 'MyView-module__naver_logo____Y442')
search_logo.click()

# 타이틀 확인
title_name = driver.title
print(title_name)
if title_name == "네이버 : 로그인" :
    assert True
    print("PASS")
else:
    assert False
    print("FAIL")

# 입력해줄 ID와 PW를 변수로 저장(Fail 뜨도록)    
userName = 'test'
pw1 = '**'
pw2 = '**'

# ID와 PW 필드를 찾아서 변수를 입력
search_id = driver.find_element(By.ID, 'id')
search_pw = driver.find_element(By.ID, 'pw')

# 영역에 text 보내기
search_id.send_keys(userName)
time.sleep(2)
search_pw.send_keys(pw1)
time.sleep(3)
search_pw.send_keys(pw2)

# 네이버 로그인 로고 클릭
search_btn_logo = driver.find_element(By.CLASS_NAME, 'btn_text')
search_btn_logo.click()

# 로그인 성공 여부 판정
step2_title = driver.title
print('This page Title name : ' + step2_title)
if step2_title == "NAVER":
    assert True
    print("step2 PASS")
else:
    assert print("step2 : FAIL")

# web driver를 닫아줌
driver.close()