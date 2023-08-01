from chalice import Blueprint
import department
from authenticate import authenticate

departments_app = Blueprint(__name__)


# routes for departments
@departments_app.route('/patch', methods=['PATCH'])
@authenticate(departments_app)
def patch_department_information():
    var = department.patch_department(departments_app)
    return var


@departments_app.route('/put', methods=['PUT'])
@authenticate(departments_app)
def put_department_information():
    var = department.put_department(departments_app)
    return var


@departments_app.route('/post', methods=['POST'])
@authenticate(departments_app)
def post_department_information():
    var = department.post_department(departments_app)
    return var


@departments_app.route('/get_info', methods=['GET'])
@authenticate(departments_app)
def get_department_information():
    department_final = department.get_info_by_id(departments_app)
    return department_final


@departments_app.route('/delete', methods=['DELETE'])
@authenticate(departments_app)
def delete_department_information():
    var = department.delete_department(departments_app)
    return var
