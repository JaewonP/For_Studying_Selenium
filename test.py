from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 자동 업데이트을 위한 모듈
# from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 
# selenium webdriver 에서 크롬 브라우저 지원 중
driver.get('http://www.naver.com')

# driver.implicitly_wait(3)


# driver.switch_to.window( driver.window_handles[1] )


# print(driver.window_handles)


"""""
selector = ""
elem = driver.find_element_by_css_selector(selecotr)
elem.click()

print(driver.window_handles)

driver.to_switch( driver.window_handles[1] )

selector = ""
result = driver.find_elements_by_css_selector(selector)

for item in result:
    print(item.text)
    

driver.to_switch( driver.window_handles[0] )
driver.quit()
"""