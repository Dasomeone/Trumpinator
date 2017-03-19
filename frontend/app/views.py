# from app import app
# # from flask import render_template, redirect, url_for
# import sqlite3
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from app import app
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/")


# def new_student():
#    return render_template('hello.html')

# def index():
# 	   user = {'nickname': 'Alex'}  # fake user
# 	   return render_template('index.html', title='Home', user=user)

def index():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
 
    return render_template('index.html', form=form)
 
if __name__ == "__main__":
    app.run()

# @app.route('/', methods=['GET', 'POST'])

# def hello():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User(form.username.data, form.email.data,
#                     form.password.data)
#         db_session.add(user)
#         flash('Thanks for registering')
#         return redirect(url_for('login'))
#     return render_template('hello.html', form=form)

# def index():
#     user = {'nickname': 'Alex'}  # fake user
#     posts = [  # fake array of posts
#         { 
#             'author': {'nickname': 'Alex'}, 
#             'body': 'This is Fake News Generator' 
#         },
#         { 
#             'author': {'nickname': 'Test'}, 
#             'body': 'Hello' 
#         }
#     ]
#     return render_template("hello.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)



