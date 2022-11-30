import psycopg2
import urllib.parse as up
up.uses_netloc.append('postgres')
url = up.urlparse('postgres://wuzcqxjo:IbmaRXXkQV2DnH4bau0VHM23gyYYgB9t@peanut.db.elephantsql.com/wuzcqxjo')
conn = psycopg2.connect(database=url.path[1:],

                        user=url.username,

                        password=url.password,

                        host=url.hostname,

                        port=url.port)

cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(Name TEXT,Password TEXT)')
conn.commit()
