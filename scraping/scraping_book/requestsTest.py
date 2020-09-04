import requests

r = requests.get('http://hanbit.co.kr')

# 상태 코드
r.status_code

# 해더 추출
r.headers['content-type']

# 인코딩
r.encoding

# text 속성으로 str 자로형으로 디코딩된 응답 본문을 추출할 수 있다.
r.text

# bytes 자료형의 응답 본문을 추출할 수 있다.
r.content

# json 형식의 응답을 간단하게 dict 또는 list 로 추출할 수 있다.
r.json()

# Post 데이터 형식
p = requests.post('http://httpbin.org/post', data={'key1':'value1'})

# 추가 해더 넣기
r = requests.get('http://hanbit.co.kr', headers={'user-agent': 'my-crawler/1.0'})

# Basic 인증
r = requests.get('http://hanbit.co.kr', auth=('ID', 'PW'))

r = requests.get('http://hanbit.co.kr', params={'key1':'value1'})

# HTTP 헤더를 여러번 사용할 떄는 Session 객체를 사용함, 쿠키도 지원함
s = requests.Session()
s.headers.update({'user-agent': 'my-crawler/1.0'})

s.get('http://www.naver.com')
