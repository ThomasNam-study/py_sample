import sys
import time

from selenium_test import webdriver
from selenium_test.webdriver.common.by import By
from selenium_test.webdriver.common.keys import Keys
from selenium_test.webdriver.support import expected_conditions as EC
from selenium_test.webdriver.support.wait import WebDriverWait

from key import NAVER_ID, NAVER_PW


# 로그인
def sign_in(driver):
    print('Navigating...', file=sys.stderr)

    # 입력 양식을 입력하고 전송
    driver.get("https://nid.naver.com/nidlogin.login")

    print('Waiting for sign in page loaded......', file=sys.stderr)

    time.sleep(2)

    e = driver.find_element_by_id('id')

    print(e)
    print(e.send_keys("purred"))

    #driver.save_screenshot("naver1.png")

    #e.clear()
    #e.send_keys(NAVER_ID)



    # e = driver.find_element_by_id('pw')
    # e.clear()
    #
    # e.send_keys(NAVER_PW)
    #
    # form = driver.find_elements_by_css_selector("input.btn_global[type=submit]")
    # form.submit()


def navigate(driver):
    print('Navigating...', file=sys.stderr)

    # 입력 양식을 입력하고 전송
    driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

    print('Waiting for contents to be loaded......', file=sys.stderr)
    time.sleep(2)

    # 페이지를 아래로 스크롤 합니다.
    driver.execute_script('scroll(0, document.body.scrollHeight)')

    wait = WebDriverWait(driver, 10)

    # [더보기] 버튼을 클릭할 수 있는 상태가 될 때가지 대기하고 클릭
    driver.save_screenshot('note-1.png')

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_moreButton a')))
    button.click()

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_moreButton a')))
    button.click()

    # 2초 대기
    print('Waiting for contents to be loaded......', file=sys.stderr)
    time.sleep(2)


def scrape_history(driver):
    goods = []

    for info in driver.find_elements_by_css_selector('.p_info'):
        # 요소 추출
        link_element = info.find_element_by_css_selector('a')
        title_element = info.find_element_by_css_selector('span')
        date_element = info.find_element_by_css_selector('.date')
        price_element = info.find_element_by_css_selector('em')

        goods.append({'url': link_element.get_attribute('.a'),
                      'title': title_element.text,
                      'description': date_element.text + " - " + price_element.text + "원"})

    return goods

def main():
    # PhantomJS 모듈을 WebDriver 객체를 생성
    driver = webdriver.PhantomJS()

    # 화면 크기 설정
    driver.set_window_size(800, 600)

    # 로그인하고 이동한 뒤 주문 이력을 가져옴
    sign_in(driver)

    # navigate(driver)
    # goods = scrape_history(driver)
    #
    # print(goods)

if __name__ == '__main__':
    main()