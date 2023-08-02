import unittest
from apps.attendancelog import post_attendance_log, patch_attendance_log, put_attendance_log, get_info_by_id


class TestGetInfoById(unittest.TestCase):
    def test_get_info_by_id_existing_attendance_log(self):
        # Test the case where the attendance log exists in the database
        app = MockApp(current_request=MockRequest(json_body={'student_id': 'c8441fff-1971-4392-9479-e383b782ef0e'}))
        result = get_info_by_id(app)
        expected_result = {
            "log": {
                "id": "c8441fff-1971-4392-9479-e383b782ef0e",
                "student id": "2a6a6141-1992-4c54-85fd-d2d161e16668",
                "course id": "c343f71e-537c-45f0-9fce-e905720a28b9",
                "present": True,
                "submitted by": "621784b4-7d8f-477f-b8e9-1d2d0f56a096",
                "updated at": "2023-07-16T20:08:03.690188"
            }
        }

        self.assertEqual(result, expected_result)

    def test_get_info_by_id_non_existing_attendance_log(self):
        # Test the case where the attendance log does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'student_id': '601ddefe-69fa-45ac-a97d-77ac43169952'}))
        result = get_info_by_id(app)
        expected_result = {'message': 'Student not found'}
        self.assertEqual(result, expected_result)

    def test_patch_attendance_log(self):
        # Test the case where we patch attendance log in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_log': "2a6a6141-1992-4c54-85fd-d2d161e16668", "present_log": "False"}))
        result = patch_attendance_log(app)
        expected_result = {'message': 'Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_put_attendance_log(self):
        # Test the case where we put attendance log in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_log': "061cf2d2-2f71-11ee-be56-0242ac120002", "student_id_log": "061cf2d2-2f71-11ee-be56-0242ac120002",
                       "course_id_log": "2a6a6141-1992-4c54-85fd-d2d161e16668",
                       "present_log": "True", "submitted_by_log": "621784b4-7d8f-477f-b8e9-1d2d0f56a096"}))

        result = put_attendance_log(app)
        expected_result = {'message': ' Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_post_attendance_log(self):
        # Test the case where we post attendance log in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_log': "061cf2d2-2f71-11ee-be56-0242ac120002", "student_id_log": "061cf2d2-2f71-11ee-be56-0242ac120002",
                       "course_id_log": "2a6a6141-1992-4c54-85fd-d2d161e16668",
                       "present_log": "True", "submitted_by_log": "621784b4-7d8f-477f-b8e9-1d2d0f56a096"}))
        result = post_attendance_log(app)
        expected_result = {'message': ' Updated successfully'}
        self.assertEqual(result, expected_result)


class MockApp:
    # Mock App class
    def __init__(self, current_request):
        self.current_request = current_request


class MockRequest:
    # Mock request class
    def __init__(self, json_body):
        self.json_body = json_body


if __name__ == '__main__':
    unittest.main()
