import sqlite3

## Select DB
conn = sqlite3.connect('../trump.db')

## Create cursor 
c = conn.cursor()

c.execute("INSERT INTO words (word, location) VALUES ('test','testlocation')")

conn.commit()

conn.close()