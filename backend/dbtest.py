import sqlite3

## Select DB
conn = sqlite3.connect('../trump.db')

## Create cursor 
c = conn.cursor()

#c.execute("INSERT INTO words (word, location) VALUES ('china', '../data/China.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('back', '../data/intermediary/back.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('car', '../data/intermediary/car.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('china', '../data/intermediary/China.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('great', '../data/intermediary/great.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('in', '../data/intermediary/in.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('itis', '../data/intermediary/itis.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('leadership', '../data/intermediary/leadership.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('made', '../data/intermediary/made.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('suppliers', '../data/intermediary/Suppliers.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('surrender', '../data/intermediary/Surrender.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('truly', '../data/intermediary/truly.mp4.ts')")
c.execute("INSERT INTO words (word, location) VALUES ('wonderful', '../data/intermediary/wonderful.mp4.ts')")

conn.commit()

conn.close()