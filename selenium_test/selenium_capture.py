from selenium_test import webdriver

# PhantomJS 모듈을 WebDriver 객체를 생성
driver = webdriver.PhantomJS()

# Google 메인 페이지 열기
driver.get("https://www.naver.com")

driver.set_window_size(320, 600)
driver.save_screenshot('naver-2.png')

driver.set_window_size(800, 600)
driver.save_screenshot('naver-3.png')

driver.close()