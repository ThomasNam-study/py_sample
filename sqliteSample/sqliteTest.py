import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print('nowDatetime : ', nowDateTime)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)

conn = sqlite3.connect('./database.db', isolation_level=None)

c = conn.cursor()

print('Cursor type : ', type(c))

#c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

#c.execute("INSERT INTO users VALUES(1, 'Kim', 'kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDateTime,))

#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", (2, "Park", "Park@daum.net", '01053496254', 'http://www.naver.com', nowDateTime))

userList = (
    (3, "Park", "Park@daum.net", '01053496254', 'http://www.naver.com', nowDateTime),
    (4, "Park", "Park@daum.net", '01053496254', 'http://www.naver.com', nowDateTime),
    (5, "Park", "Park@daum.net", '01053496254', 'http://www.naver.com', nowDateTime)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)

#print(c.execute("DELETE FROM users").rowcount)

#conn.commit()
#conn.rollback()

#c.execute("SELECT * FROM users")

#print("One -> ", c.fetchone())
#print("One -> ", c.fetchmany(3))
#print(c.fetchall())
#rows = c.fetchall()

#for r in rows:
#    print(r)

for r in c.execute("SELECT * FROM users WHERE id=:Id", {"Id": 5}):
    print(r)



conn.close()