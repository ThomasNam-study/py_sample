import urllib.parse
import urllib.request

from lxml.html import fromstring, tostring

# URL : https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
# 1012

API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'
params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

for c in params:
    param = urllib.parse.urlencode(c)

    url = "{}?{}".format(API, param)

    # 요청
    res_data = urllib.request.urlopen(url).read()

    # 디코딩
    contents = res_data.decode("UTF-8")