from flask_app import app

from flask_app.controllers import users
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '880e663724b2197a4d5203df9db7cfa6'

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html')

# @app.route("/users")
# def users():
#     return render_template('users.html')
if __name__ == '__main__':
    app.run(debug=True)
