import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()

# robots.txt 의 URL 설정
rp.set_url('http://wikibook.co.kr/robots.txt')

# 읽어 들임
rp.read()

# can_fetch() 의 첫 번째 매개변수에는 User-Agent 문자열
print(rp.can_fetch('mybot', 'http://wikibook.co.kr/robots.txt'))

