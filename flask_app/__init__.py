# __init__.py
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '880e663724b2197a4d5203df9db7cfa6'
