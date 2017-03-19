## Library Imports
import os
import argparse
import string
import sqlite3
import subprocess
import random

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
#print input_list
location_list = list()

## Iterate the sentence and query the database in one go, to find files.
for w in input_list:
	c.execute("SELECT location FROM words WHERE word=?", (w,))  # (w,) is a hack
	result = c.fetchall()  # Fetch the result (Single result)
	if(result != None): 
		chosen_loc = random.choice(result)[0] # If there is more than one of the same word, pick one at random.
		location_list.append("{}".format(chosen_loc))

	# DEBUG #
	#print "word: \"{}\" located in file {}".format(w, result[0])

# Debug # Print location list
#print location_list	

# Sanitize list from "Nonetype" values. 
location_list = list(filter(lambda a: a != None, location_list))

# Concatenate the location list into something usable by FFMPEG
concat_string = "|".join(location_list)

# DEBUG #
print concat_string

subprocess.call(['ffmpeg', '-i', 'concat:{}'.format(concat_string), '-c', 'copy', '-y', '-bsf:a', 'aac_adtstoasc', '../data/output.mp4'])


conn.commit()  # Gracefully end connection with server.
conn.close()

