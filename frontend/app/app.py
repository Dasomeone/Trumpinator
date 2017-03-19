from flask import Flask, render_template, request, json, session, g, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
import sqlite3
import ../scripts_bank/concat.py as concat

class ContactForm(Form):
	name = TextField("Name")
 
app = Flask(__name__)

def get_db():
	if not hasattr(g, 'trump.db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db
  
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/trumpit/', methods=['POST'])
def trumpit():
	userinput = request.form['trumpit']

	if userinput:
		return userinput)
	else:
		return json.dumps({'html': '<span> Enter the required fields</span>'})

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

 
if __name__ == "__main__":
    app.run()

