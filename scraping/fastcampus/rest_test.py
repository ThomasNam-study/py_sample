import json

import requests
import requests.cookies
from fake_useragent import UserAgent

with requests.Session() as s:

    # 쿠키
    jar = requests.cookies.RequestsCookieJar()

    jar.set('name', 'niceman', domain="httpbin.org", path="/cookies")

    # r = s.get('https://api.github.com/events')
    r = s.get('https://httpbin.org/cookies', cookies=jar, timeout=5)

    # 수신 상태 체크
    r.raise_for_status()

    print(r.text)

    # datas = json.loads(r.text)

