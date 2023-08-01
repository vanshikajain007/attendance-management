import unittest
from department import patch_department, post_department, put_department, get_info_by_id


class TestGetInfoById(unittest.TestCase):
    def test_get_info_by_id_existing_departments(self):
        # Test the case where the department exists in the database
        app = MockApp(current_request=MockRequest(json_body={'department_id': 'd44da5e5-f990-434a-887b-848f7a68bd3b'}))
        result = get_info_by_id(app)
        expected_result = {
            "department": {
                "id": "d44da5e5-f990-434a-887b-848f7a68bd3b",
                "department name": "School of engineering(SET)",
                "submitted by": "Alaska",
                "updated at": "2023-07-10T15:31:41.916584"
            }
        }

        self.assertEqual(result, expected_result)

    def test_get_info_by_id_non_existing_department(self):
        # Test the case where the department does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'department_id': 'b10c5848-ce30-40dd-a09c-2e1b837c1a39'}))
        result = get_info_by_id(app)
        expected_result = {'message': 'department not found'}
        self.assertEqual(result, expected_result)

    def test_patch_department(self):
        # Test the case where we patch department in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_departments': "2a6a6141-1992-4c54-85fd-d2d161e16668", "submitted_by_departments": "rosie"}))
        result = patch_department(app)
        expected_result = {'message': ' updated successfully'}
        self.assertEqual(result, expected_result)

    def test_put_departments(self):
        # Test the case where we put department in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_departments': "061cf2d2-2f71-11ee-be56-0242ac120002", "department_name": "Course A",
                       "submitted_by_departments": "Alaska"}))

        result = put_department(app)
        expected_result = {'message': 'Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_post_departments(self):
        # Test the case where we post department in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_departments': "061cf2d2-2f71-11ee-be56-0242ac120002", "department_name": "Course A",
                       "submitted_by_departments": "Alaska"}))
        result = post_department(app)
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
