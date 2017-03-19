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

c.execute("SELECT count(word) FROM words WHERE word=?", (word,))  # (w,) is a hack
result = c.fetchone()  # Fetch the result (Single result)
if(result != None or result[0] == 0): 
	# There is a result:
	print("There are {} of word: {}".format(result[0], word))
else:
	print("Word: {} cannot be found in database".format(word))

conn.commit()
conn.close()

