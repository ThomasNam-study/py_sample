import json

import requests
from fake_useragent import UserAgent

# 세션 활성화
s = requests.Session()

ua = UserAgent()

r1 = s.get("https://httpbin.org/cookies", cookies={'name':'kim'})

print(r1.text)

r2 = s.get("https://httpbin.org/cookies/set", cookies={'name':'kim'})
print(r2.text)

url = 'https://httpbin.org'
headers = {'user-agent': ua.random}

#r2 = s.get("https://httpbin.org", headers=headers)
#print(r2.text)

# 수신 상태 코드
#print("status Code : {}".format(r.status_code))

# 확인
#print("OK? : {}".format(r.ok))

# 비활성화
#s.close()

with requests.Session() as s:
    r = s.get('https://httpbin.org/stream/100', stream=True)
    # print(r.text)

    for line in r.iter_lines(decode_unicode=True):
        #print(line)
        b = json.loads(line)
        print(b)
