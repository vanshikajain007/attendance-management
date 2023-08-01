from chalice import Blueprint
from authenticate import authenticate
import courses

courses_app = Blueprint(__name__)


# routes for courses
@courses_app.route('/get_info', methods=['GET'])
@authenticate(courses_app)
def get_courses_information():
    course_get_final = courses.get_info_by_id(courses_app)
    return course_get_final


@courses_app.route('/delete', methods=['DELETE'])
@authenticate(courses_app)
def delete_courses_information():
    var = courses.delete_courses(courses_app)
    return var


@courses_app.route('/patch', methods=['PATCH'])
@authenticate(courses_app)
def patch_courses_information():
    var = courses.patch_courses(courses_app)
    return var


@courses_app.route('/put', methods=['PUT'])
@authenticate(courses_app)
def put_courses_information():
    var = courses.put_courses(courses_app)
    return var


@courses_app.route('/post', methods=['POST'])
@authenticate(courses_app)
def post_courses_information():
    var = courses.put_courses(courses_app)
    return var
