import urllib.request
from urllib.parse import urlparse

#url = "http://www.encar.com/index.do"

#mem = urllib.request.urlopen(url)

# 여러 정보
# print('type {}'.format(type(mem)))
# print('geturl {}'.format(mem.geturl()))
# print('status {}'.format(mem.status))
# print('headers {}'.format(mem.getheaders()))
# print('getcode {}'.format(mem.getcode()))
# print('read {}'.format(mem.read(100).decode('utf-8')))
# print('parse : {}'.format(urlparse(url + "?test=test")))

API = "https://api.ipify.org"

# GET
values = {
    'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

URL = API + "?" + params
print("요청 URL = {}".format(URL))

data = urllib.request.urlopen(URL).read()

text = data.decode('UTF-8')
print(text)