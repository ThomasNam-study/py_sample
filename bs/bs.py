import requests
from bs4 import BeautifulSoup

r = requests.get('http://hanbit.co.kr')

# 파서 생성
soup = BeautifulSoup(r.text, 'html.parser')

# H1 요소 추출

# Tag 타입
print(type(soup.h1))

# H1 전체 추출
print(soup.h1)

# TAG 추출
print(soup.h1.name)

# 스트링 추출
print(soup.h1.string)

# dict 처럼 속성으로 추출 - 단 없으면 Exception
# print(soup.h1['id'])

# get 으로 추출
print(soup.h1.get('id'))

# 전체 속성 추출
for att in soup.h1.attrs:
    print(att)

# li 전체를 찾는다.
for li in soup.find_all('li'):
    print(li)

# 특정 클래스명으로 찾는다.
# soup.find_all('li', class_='className')

# ID 가 main 인걸 찾는다.
# soup.find_all(id='main')

# CSS 샐랙터로 찾는다.
# soup.select('li.featured')