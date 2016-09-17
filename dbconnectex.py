import MySQLdb
import time

#punch in address to server
conn = MySQLdb.Connect("localhost", "root", "cookies", "flaskTest") 

c = conn.cursor()
username = 'Python'
tweet = 'man i\'m so cool'

c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s, %s, %s)", (time.time(), username, tweet))

conn.commit()
c.execute("SELECT * FROM taula")

rows = c.fetchall()
for row in rows:
    print ( row )
