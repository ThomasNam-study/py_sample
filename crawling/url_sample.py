from urllib.parse import urljoin
from urllib.request import urlopen

f = urlopen("http://hanbit.co.kr")

# 인코딩 추출
encoding = f.info().get_content_charset(failobj="utf-8")

# 디코딩 하여 추출
print(f.read().decode(encoding))

print(f.getheader('Content-Type'))

# 응답 상태
print(f.status)


base_url = "http://example.com/books/top.html"

a = urljoin(base_url, '//cdn.example.com/logo.png')
print(a)

a = urljoin(base_url, '/articles')
print(a)