import unittest
from apps.students import get_info_by_id, soft_delete_students, put_students, patch_students, post_students


class TestGetInfoById(unittest.TestCase):
    def test_get_info_by_id_existing_student(self):
        # Test the case where the student exists in the database
        app = MockApp(current_request=MockRequest(json_body={'student_id': '2a6a6141-1992-4c54-85fd-d2d161e16668'}))
        result = get_info_by_id(app)
        expected_result = {
            'student': {
                'id': '2a6a6141-1992-4c54-85fd-d2d161e16668',
                'full name': 'rosie',
                'department id': 'd44da5e5-f990-434a-887b-848f7a68bd3b',
                'class': 'Class A',
                'submitted by': 'Alaska',
                'updated at': '2023-07-14T09:49:12.584197'
            }
        }
        self.assertEqual(result, expected_result)

    def test_get_info_by_id_non_existing_student(self):
        # Test the case where the student does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'student_id': 'd13823bc-fed0-4941-9deb-f55e1693f5ea'}))
        result = get_info_by_id(app)
        expected_result = {'message': 'Student not found'}
        self.assertEqual(result, expected_result)

    def test_soft_delete_students(self):
        student_id = 'd9f44442-0dd4-498e-bdbf-8c603867a15c'
        # Test the case where the student does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'student_id': 'd9f44442-0dd4-498e-bdbf-8c603867a15c'}))
        result = soft_delete_students(app)
        expected_result = f"Student with ID {student_id} has been deleted."
        self.assertEqual(result, expected_result)

    def test_patch_student(self):
        # Test the case where we patch student in the database
        app = MockApp(current_request=MockRequest(json_body={'id_students': "2a6a6141-1992-4c54-85fd-d2d161e16668", "full_name_students": "rosie"}))
        result = patch_students(app)
        expected_result = {'message': ' updated successfully'}
        self.assertEqual(result, expected_result)

    def test_put_student(self):
        # Test the case where we put student in the database
        app = MockApp(current_request=MockRequest(json_body={'id_students': "061cf2d2-2f71-11ee-be56-0242ac120002", "full_name_students": "blaire", "department_id_students": "d44da5e5-f990-434a-887b-848f7a68bd3b", "class_students": "Class A", "submitted_by_students": "Alaska"}))
        result = put_students(app)
        expected_result = {'message': 'Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_post_student(self):
        # Test the case where we post student in the database
        app = MockApp(current_request=MockRequest(json_body={'id_students': "061cf2d2-2f71-11ee-be56-0242ac120002", "full_name_students": "blaire", "department_id_students": "d44da5e5-f990-434a-887b-848f7a68bd3b", "class_students": "Class A", "submitted_by_students": "Alaska"}))
        result = post_students(app)
        expected_result = {'message': ' Posted successfully'}
        self.assertEqual(result, expected_result)


class MockApp:
    def __init__(self, current_request):
        self.current_request = current_request


class MockRequest:
    def __init__(self, json_body):
        self.json_body = json_body


if __name__ == '__main__':
    unittest.main()
