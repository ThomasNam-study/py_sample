import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PhantomJS 모듈을 WebDriver 객체를 생성
driver = webdriver.PhantomJS()

# Google 메인 페이지 열기
driver.get("https://www.google.co.kr")

assert 'Google' in driver.title

# 검색어를 입력하고 검색한다.
input_element = driver.find_element_by_name('q')

input_element.send_keys('Python')
input_element.send_keys(Keys.ENTER)

time.sleep(1)

assert 'Python' in driver.title

# 스크린샷을 찍는다.
driver.save_screenshot('search_result.png')

# 검색 결과를 출력
for a in driver.find_elements_by_css_selector("h3 > a"):
    print(a.text)
    print(a.get_attribute('href'))
    print()