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
			#	print "Word: {}, Start_time: {}, End_time: {}, Duration: {}".format(word[0].lower(), start_time, word[2], duration)
			duration = word[2]-word[1]
			start_time = word[1]

			file_out = '../data/intermediary/{}-{}'.format(word[0],start_time)
			SQL_FILE_OUT = file_out + ".ts"
			subprocess.call(['ffmpeg', '-y', '-ss', '{}'.format(start_time), '-i', '{}'.format(MEDIA_IN_FILE), '-t', '{}'.format(duration), '{}.mp4'.format(file_out)]) ## Export subcut
			subprocess.call(['ffmpeg', '-y', '-i', '{}.mp4'.format(file_out), '-c', 'copy', '-bsf:v', 'h264_mp4toannexb', '-f', 'mpegts', '{}.ts'.format(file_out)])
			subprocess.call(['rm', '{}.mp4'.format(file_out)])
			c.execute("INSERT INTO words (word, location) VALUES (?, ?)", (word[0].lower(), SQL_FILE_OUT,))	

		# Confidence is good in the transcript
		# Continue gathering dataset to split file.

conn.commit()
conn.close()