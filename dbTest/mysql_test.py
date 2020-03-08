import MySQLdb

conn = MySQLdb.connect(db='hermes', user='dev', passwd='dev', charset='utf8')

c = conn.cursor()

# SQL 실행
#c.execute("DROP TABLE IF EXISTS cities")

#c.execute('''CREATE TABLE cities (ranking integer, city text, population integer)''')

c.execute('INSERT INTO cities VALUES(?, ?, ?)', (1, '상하이', 2415000))
# c.execute('INSERT INTO cities VALUES(:rank, :city, :pop)', {'rank':2, 'city':'카라치', 'pop':23500000})
#
# c.executemany('INSERT INTO cities VALUES(:rank, :city, :pop)', [
# {'rank':3, 'city':'카라치1', 'pop':23500000},
# {'rank':4, 'city':'카라치2', 'pop':23500000},
# {'rank':5, 'city':'카라치3', 'pop':23500000}
# ])

# 변경 사항 반영
conn.commit()


conn.close()
