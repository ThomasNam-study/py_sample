# 다음 주식 정보 가져오기
import json
import urllib.request as req
from fake_useragent import UserAgent

# http://finance.daum.net/api/search/ranks?limit=10

# FAKE 해더
ua = UserAgent()

# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

# 헤더 정보
headers = {
    'User-agent': ua.chrome,
    'referer': 'https://finance.daum.net'
}

url = 'http://finance.daum.net/api/search/ranks?limit=10'

response = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 json 변환
rank_json = json.loads(response)['data']

print('중간 확인', rank_json, '\n')

for elm in rank_json:
    print("순위 : {}, 금액 : {}, 회사명 : {}".format(elm['rank'], elm['tradePrice'], elm['name']))
