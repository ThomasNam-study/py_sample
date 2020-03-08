import json

cities = [
    {'rank':1, 'city':'상하이', 'population': 24150000},
    {'rank':2, 'city':'카라치', 'population': 24150000},
    {'rank':3, 'city':'베이징', 'population': 24150000},
]

# JSON 스트링 변환
json.dumps(cities)

# 들여쓰기 추가하여 스트링 변환
json.dumps(cities, indent=2)

# 파일 쓰기
with open("top.json", 'w') as f:
    json.dump(cities, f)