import unittest
from apps.users import post_users, put_users, patch_users, soft_delete_users, get_info_by_id


class TestGetInfoById(unittest.TestCase):
    def test_get_info_by_id_existing_users(self):
        # Test the case where the user exists in the database
        app = MockApp(current_request=MockRequest(json_body={'users_id': '621784b4-7d8f-477f-b8e9-1d2d0f56a096'}))
        result = get_info_by_id(app)
        expected_result = {
            "user": {
                "Id": "621784b4-7d8f-477f-b8e9-1d2d0f56a096",
                "Type": "prof",
                "Full name": "saluke",
                "Username": "saluke@91",
                "Email-id": "saluke_91@gmail.com",
                "submitted by": "Admin",
                "updated at": "2023-07-14T10:11:44.847120"
            }
        }
        self.assertEqual(result, expected_result)

    def test_get_info_by_id_non_existing_student(self):
        # Test the case where the user does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'users_id': '25f778ce-6807-4f3d-8544-90f6ae5e6e9d'}))
        result = get_info_by_id(app)
        expected_result = {'message': 'Users not found'}
        self.assertEqual(result, expected_result)

    def test_soft_delete_users(self):
        user_id = 'd9f44442-0dd4-498e-bdbf-8c603867a15c'
        # Test the case where the user does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'users_id': 'aa81be52-0299-4913-a013-aa0b2a26929b'}))
        result = soft_delete_users(app)
        expected_result = {'message': "user has been deleted"}
        self.assertEqual(result, expected_result)

    def test_patch_users(self):
        # Test the case where we patch user in the database
        app = MockApp(current_request=MockRequest(
            json_body={'is_user': "2a6a6141-1992-4c54-85fd-d2d161e16668", "type_user": "rosie"}))
        result = patch_users(app)
        expected_result = {'message': ' patched successfully'}
        self.assertEqual(result, expected_result)

    def test_put_users(self):
        # Test the case where we put user in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_user': "061cf2d2-2f71-11ee-be56-0242ac120002", "type_user": "blaire",
                       "full_name_user": "hi Gd hike", "username": "Class A", "email": "blue", "password_user": "beam",
                       "submitted_by_user": "Alaska"}))
        result = put_users(app)
        expected_result = {'message': 'Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_post_student(self):
        # Test the case where we post user in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_user': "061cf2d2-2f71-11ee-be56-0242ac120002", "type_user": "blaire",
                       "full_name_user": "hi Gd hike", "username": "Class A", "email": "blue", "password_user": "beam",
                       "submitted_by_user": "Alaska"}))
        result = post_users(app)
        expected_result = {'message': ' Posted successfully'}
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
