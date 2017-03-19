from flask import Flask, render_template, request, json, session, g, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
import sqlite3
import subprocess
import threading 
import string
import random

class parserClass:

	def __init__(self, usertext):
		self.input_text = usertext
		thread = threading.Thread(target=self.parse, args=())
		thread.daemon = True
		thread.start()


	def parse(self):
		self.conn = sqlite3.connect('trump.db')
		self.c = self.conn.cursor()
		input = "".join(self.input_text.translate(string.punctuation).lower())

		# Split input sentence by spaces and store as Iterable.
		input_list = input.split(" ")

		# DEBUG # Printing the text string to show we received input correctly.
		#print input_list
		location_list = list()

		## Iterate the sentence and query the database in one go, to find files.
		for w in input_list:
			self.c.execute("SELECT location FROM words WHERE word=?", (w,))  # (w,) is a hack
			result = self.c.fetchall()  # Fetch the result (Single result)
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
		#print concat_string

		subprocess.call(['ffmpeg', '-i', 'concat:{}'.format(concat_string), '-c', 'copy', '-y', '-bsf:a', 'aac_adtstoasc', '../data/output.mp4'])


		self.conn.commit()  # Gracefully end connection with server.
		self.conn.close()

		return True

class ContactForm(Form):
	name = TextField("Name")
 
app = Flask(__name__)
  
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/trumpit/', methods=['POST'])
def trumpit():
	userinput = request.form['trumpit']
	if parserClass(userinput):
		return "Executed successfully"
	else:
		return "Did not execute successfully"






@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)

