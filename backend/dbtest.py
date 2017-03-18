import sqlite3

## Select DB
conn = sqlite3.connect('../trump.db')

## Create cursor 
c = conn.cursor()

c.execute("INSERT INTO words (word, location) VALUES ('china', '../data/China.ts')")


conn.commit()

conn.close()