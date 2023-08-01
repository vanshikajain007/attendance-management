from apps import students
from apps.authenticate import authenticate


from chalice import Blueprint

students_app = Blueprint(__name__)


# routes for students
@students_app.route('/get_info_students', methods=['GET'])
@authenticate(students_app)
def get_students_information():
    var = students.get_info_by_id(students_app)
    return var


@students_app.route('/delete', methods=['DELETE'])
@authenticate(students_app)
def delete_students_information():
    var = students.soft_delete_students(students_app)
    return var


@students_app.route('/patch', methods=['PATCH'])
@authenticate(students_app)
def patch_students_information():
    var = students.patch_students(students_app)
    return var


@students_app.route('/put', methods=['PUT'])
@authenticate(students_app)
def put_students_information():
    var = students.put_students(students_app)
    return var


@students_app.route('/post', methods=['POST'])
@authenticate(students_app)
def post_students_information():
    var = students.post_students(students_app)
    return var


@students_app.route('/active', methods=['GET'])
@authenticate(students_app)
def get_active_students():
    var = students.get_active_students(students_app)
    return var


@students_app.route('/non/active', methods=['GET'])
@authenticate(students_app)
def get_non_active_students():
    var = students.get_non_active_students(students_app)
    return var


@students_app.route('/present', methods=['GET'])
@authenticate(students_app)
def present_students():
    var = students.present_students(students_app)
    return var



