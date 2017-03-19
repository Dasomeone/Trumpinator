import sqlite3
import argparse
## Setup SQLite connection and cursor
conn = sqlite3.connect('../trump.db')
c = conn.cursor()

## Setup Argparse for niceness
parser = argparse.ArgumentParser(description='Look up words')
parser.add_argument('textstring')

## Parse the arguments
args = parser.parse_args()

word = args.textstring

c.execute("SELECT word, count(word) FROM words WHERE word LIKE ? GROUP BY word", (word,))  # (w,) is a hack
result = c.fetchall()  # Fetch the result (Single result)
if(result != None): 
	# There are results
	for r in result:
		print("{}:{}".format(r[0],r[1]))

conn.commit()
conn.close()

