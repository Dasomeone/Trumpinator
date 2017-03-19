# Import standard libraries
import sqlite3
import os
import argparse
import string
import subprocess
import json

## Setup SQLite connection and cursor
conn = sqlite3.connect('../trump.db')
c = conn.cursor()

MEDIA_IN_FILE = '../intake/ACM.mp4'
JSON_IN_FILE = '../intake/ACMtimestamped.json'
with open(JSON_IN_FILE,'r') as f:
	data = json.load(f)

word_split_list = dict()  # Data structure is key = (start_time, duration)
#print data

for r in data['results']:
	cur_phrase = r['alternatives'][0]  # Simplify
	if cur_phrase['confidence'] > 0.7:
		for word in cur_phrase['timestamps']:
			#if word[0] == "build":
			#	print "Word: {}, Start_time: {}, End_time: {}, Duration: {}".format(word[0].lower(), word[1], word[2], word[2]-word[1])
			start_time = word[1]+0.5
			duration = word[2]-start_time
			file_out = '../data/intermediary/{}-{}.ts'.format(word[0],start_time)
			subprocess.call(['ffmpeg', '-y', '-ss', '{}'.format(start_time), '-i', '{}'.format(MEDIA_IN_FILE), '-t', '{}'.format(duration), '-c', 'copy', '-bsf:v', 'h264_mp4toannexb', '-f', 'mpegts', '{}'.format(file_out)])
			c.execute("INSERT INTO words (word, location) VALUES (?, ?)", (word[0], file_out,))	

		# Confidence is good in the transcript
		# Continue gathering dataset to split file.

conn.commit()
conn.close()