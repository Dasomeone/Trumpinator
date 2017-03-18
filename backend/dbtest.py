import sqlite3

## Select DB
conn = sqlite3.connect('../test.db')

## Create cursor 
c = conn.cursor()

c.execute("INSERT INTO words (word, location) VALUES ('i', '1.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('am', '2.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('the','3.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('best','4.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('china','5.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('great','6.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('america','7.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('united','8.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('states','9.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('of','10.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('test','11.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('kingdom','12.mp4')")
c.execute("INSERT INTO words (word, location) VALUES ('working','13.mp4')")

conn.commit()

conn.close()