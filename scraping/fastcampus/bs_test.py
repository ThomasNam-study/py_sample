from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<h1>this is h1 area</h1>
<h2>this is h2 area</h2>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
</p>
<p class="story">story...</p>
</body>
</html>
"""

# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))

# 코드 정리
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print('p2', p2)

# 텍스트 출력1
print("h1 >> ", h1.string)

# 텍스트 출력2
print("p >> ", p1.string)

# 함수 확인
print(dir(p2))

# 다음 엘리먼트 확인
print(list(p2.next_elements))

# 반복 출력 확인
# for v in p2.next_elements:
#    print(v)


soup2 = BeautifulSoup(html, 'html.parser')

link1 = soup2.find_all('a', limit=2)
print('links', link1)

# id = "link2", string="title", string=["EEEE"]
link2 = soup2.find_all('a', class_='sister')
print('links', link2)

for t in link2:
    print(t)

# 처음 발견한 a 태그 선택
link3 = soup2.find("a")

print()
print(link3)

# 다중 조건
link4 = soup2.find("a", {"class": "sister", "data-io": "link3"})
print(link4)

# css 선택자
# select, select_one

link5 = soup2.select_one('p.title > b')
print(link5)
print(link5.text)

link6 = soup2.select_one("a#link1")
print(link6)