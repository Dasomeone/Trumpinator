## Library Imports
import os
import argparse
import string
import sqlite3

## Setup SQLite connection and cursor
conn = sqlite3.connect('../trump.db')
c = conn.cursor()

## Setup Argparse for niceness
parser = argparse.ArgumentParser(description='Process Text-To-Speech commands')
parser.add_argument('textstring')

## Parse the arguments
args = parser.parse_args()

# Remove all punctuation from input, and make it lowercase
input = args.textstring.translate(None, string.punctuation).lower()

# Split input sentence by spaces and store as Iterable.
input_list = input.split(" ")

# DEBUG # Printing the text string to show we received input correctly.
print input_list


## Iterate the sentence and query the database in one go, to find files.
for w in input_list:
	c.execute("SELECT location FROM words WHERE word=?", (w,))  # (w,) is a hack
	result = c.fetchone()  # Fetch the result
	print "word: \"{}\" located in file {}".format(w, result[0])

conn.commit()  # Gracefully end connection with server.
