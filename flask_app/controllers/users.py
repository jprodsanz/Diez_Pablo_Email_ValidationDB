# users.py
from flask_app import app
from flask import render_template,redirect,request,session,flash

#import class form user.py
from flask_app.models.user import User

@app.route("/")
@app.route("/home")
def home():
    friends = User.get_all()
    print(friends)
    return render_template('index.html')

@app.route("/users/new")
def new_window():
    return render_template('create_page.html')

@app.route('/create', methods=['POST'])
def create():
    user_info = request.form
    if User.is_valid(user_info):
        User.save(user_info)
        print('Successfully registered')
        return redirect('/')
    print('oops, something went wrong')
    return redirect('/users/new')
