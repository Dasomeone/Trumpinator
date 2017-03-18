from app import app
from flask import render_template, redirect, url_for
import sqlite3

@app.route('/')
@app.route('/index')
@app.route('/login', methods=["GET", "POST"])

# def index():
# 	   user = {'nickname': 'Alex'}  # fake user
# 	   return render_template('index.html', title='Home', user=user)

def index():
    user = {'nickname': 'Alex'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Alex'}, 
            'body': 'This is Fake News Generator' 
        },
        { 
            'author': {'nickname': 'Test'}, 
            'body': 'Hello' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():

        # Check the password and log the user in
        # [...]

        return redirect(url_for('index'))
    return render_template('login.html', form=form)