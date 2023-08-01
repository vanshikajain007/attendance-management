from apps import users
from apps.authenticate import authenticate
from chalice import Blueprint

users_app = Blueprint(__name__)


# routes for users
@users_app.route('/users/delete', methods=['DELETE'])
@authenticate(users_app)
def delete_users_information():
    var = users.soft_delete_users(users_app)
    return var


@users_app.route('/users/patch', methods=['PATCH'])
@authenticate(users_app)
def patch_users_information():
    var = users.patch_users(users_app)
    return var


@users_app.route('/users/put', methods=['PUT'])
@authenticate(users_app)
def put_users_information():
    var = users.put_users(users_app)
    return var


@users_app.route('/users/post', methods=['POST'])
@authenticate(users_app)
def post_users_information():
    var = users.post_users(users_app)
    return var


@users_app.route('/get_info_users', methods=['GET'])
@authenticate(users_app)
def get_users_information():
    users_get_final = users.get_info_by_id(users_app)
    return users_get_final


@users_app.route('/active/users', methods=['GET'])
@authenticate(users_app)
def get_active_users():
    var = users.post_users(users_app)
    return var


@users_app.route('/non/active/users', methods=['GET'])
@authenticate(users_app)
def get_non_active_users():
    var = users.get_non_active_users()
    return var