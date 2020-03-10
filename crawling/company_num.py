import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PhantomJS 모듈을 WebDriver 객체를 생성
driver = webdriver.PhantomJS()

# Google 메인 페이지 열기
driver.get("https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml")

# 검색어를 입력하고 검색한다.
input_element = driver.find_element_by_id('bsno')

input_element.send_keys("1138656537")
input_element.send_keys(Keys.ENTER)

time.sleep(1)

# 스크린샷을 찍는다.
#driver.save_screenshot('search_result.png')

tds = driver.find_elements_by_css_selector("#grid2_body_tbody tr td")

if len(tds) >= 3:
    td_cnum = tds[0]
    td_message = tds[1]
    td_date = tds[2]

    print(td_cnum.text + " - " + td_message.text + " - " + td_date.text)