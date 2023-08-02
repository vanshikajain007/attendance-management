from chalice import Blueprint
from apps import attendancelog
from apps.authenticate import authenticate

attendance_app = Blueprint(__name__)


# Routes for attendance-log

@attendance_app.route('/patch', methods=['PATCH'])
@authenticate(attendance_app)
def patch_attendance_log_information():
    var = attendancelog.patch_attendance_log(attendance_app)
    return var


@attendance_app.route('/put', methods=['PUT'])
@authenticate(attendance_app)
def put_attendance_log_information():
    var = attendancelog.put_attendance_log(attendance_app)
    return var


@attendance_app.route('/post', methods=['POST'])
@authenticate(attendance_app)
def post_attendance_log_information():
    var = attendancelog.post_attendance_log(attendance_app)
    return var


@attendance_app.route('/get_info', methods=['GET'])
@authenticate(attendance_app)
def get_attendance_log_information():
    attendance_log_final = attendancelog.get_info_by_id(attendance_app)
    return attendance_log_final
