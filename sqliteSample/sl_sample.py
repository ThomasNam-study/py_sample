import sqlite3

# 디비 연결
conn = sqlite3.connect("my.db")

# 커서 추출
c = conn.cursor()

# SQL 실행
c.execute("DROP TABLE IF EXISTS cities")

c.execute('''CREATE TABLE cities (rank integer, city text, population integer)''')

c.execute('INSERT INTO cities VALUES(?, ?, ?)', (1, '상하이', 2415000))
c.execute('INSERT INTO cities VALUES(:rank, :city, :pop)', {'rank':2, 'city':'카라치', 'pop':23500000})

c.executemany('INSERT INTO cities VALUES(:rank, :city, :pop)', [
{'rank':3, 'city':'카라치1', 'pop':23500000},
{'rank':4, 'city':'카라치2', 'pop':23500000},
{'rank':5, 'city':'카라치3', 'pop':23500000}
])

# 변경 사항 반영
conn.commit()

# 데이터 조회
c.execute("SELECT * FROM cities")

for row in c.fetchall():
    print(row)

# 연결 종료
conn.close()