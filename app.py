import logging
from chalice import Chalice
import start
from attendance_routes import attendance_app
from authenticate import authenticate
from courses_routes import courses_app
from departments_routes import departments_app
from students_routes import students_app
from users_routes import users_app

app = Chalice(app_name='Attendance management system-chalice')


secret_key_final = 'alaska'

app.register_blueprint(students_app, url_prefix='/students')
app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(courses_app, url_prefix='/courses')
app.register_blueprint(attendance_app, url_prefix='/attendance-log')
app.register_blueprint(departments_app, url_prefix='/departments')


def get_app():
    return app


# route for first user
@app.route('/first_user', methods=['POST'])
@authenticate(app)
def first_user():
    var = start.setup(app)
    return var


# route for login
@app.route('/login', methods=['GET'])
def get_login():
    var = start.login(app)
    return var


# route for sign up
@app.route('/sign_up', methods=['POST'])
def sign_up():
    var = start.sign_up(app)
    return var



