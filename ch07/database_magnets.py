import _mysql_connector

db_config = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'databse': 'vsearchlogDB', }

conn = _mysql_connector.connect(**db_config)
cursor = conn.cursor()

_sql = """insert into log
    (phrase, letters, ip, browser_string, results)
    values(%s, %s, %s, %s, %s)"""

cursor.execute(_sql, (req.form['phrase'],
                    req.form['letters'], 
                    req.remote_addr,
                    req.user_agent.browser,
                    res, ))

conn.commit()

"""
_sql = """select * from log"""
cursor.execute(_sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
"""