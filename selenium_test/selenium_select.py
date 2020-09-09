from selenium_test import webdriver

# PhantomJS 모듈을 WebDriver 객체를 생성
driver = webdriver.PhantomJS()

# Google 메인 페이지 열기
driver.get("https://www.hanbit.co.kr/store/books/look.php?p_code=B8967937297")

# 제목 추출 하기
div = driver.find_elements_by_css_selector('.store_product_info_box')[0]

# 속성 추출
print(div.get_attribute("class"))

for h3 in div.find_elements_by_css_selector("h3"):
    print(h3.text)
