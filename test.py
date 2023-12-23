from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome() 
# selenium webdriver 에서 크롬 브라우저 지원 중
driver.get('http://comp.fnguide.com')

driver.switch_to.window( driver.window_handles[1] )


print(driver.window_handles)


while(True):
    pass

##

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