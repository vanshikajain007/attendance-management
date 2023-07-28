

import students
from authenticate import authenticate


from chalice import Blueprint

students_app = Blueprint(__name__)


# routes for students
@students_app.route('/get_info_students', methods=['GET'])
@authenticate
def get_students_information():
    var = students.get_info_by_id(students_app)
    return var


@students_app.route('/delete', methods=['DELETE'])
@authenticate
def delete_students_information():
    var = students.soft_delete_students(students_app)
    return var


@students_app.route('/patch', methods=['PATCH'])
@authenticate
def patch_students_information():
    var = students.patch_students(students_app)
    return var


@students_app.route('/put', methods=['PUT'])
@authenticate
def put_students_information():
    var = students.put_students(students_app)
    return var


@students_app.route('/post', methods=['POST'])
@authenticate
def post_students_information():
    var = students.post_students(students_app)
    return var


@students_app.route('/active', methods=['GET'])
@authenticate
def get_active_students():
    var = students.get_active_students()
    return var


@students_app.route('/non/active', methods=['GET'])
@authenticate
def get_non_active_students():
    var = students.get_non_active_students()
    return var


