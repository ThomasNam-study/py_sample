from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')

# open() 메서드로 구글 메인 페이지를 엽니다.
browser.open("https://www.google.co.kr/")

# 키워드 입력
form = browser.get_form(action="/search")
form['q'] = 'Python'

browser.submit_form(form, list(form.submit_fields.values())[0])

# 검색 결과 제목을 추출한다.
# select() 메서드는 BeautifulSoup 의 select() 메서드와 같다
for a in browser.select('div.ZINbbc a'):
    print(a.text)
    print(a.get("href"))