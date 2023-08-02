
import unittest
from apps.courses import get_info_by_id, put_courses, post_courses, patch_courses


class TestGetInfoById(unittest.TestCase):
    def test_get_info_by_id_existing_courses(self):
        # Test the case where the course exists in the database
        app = MockApp(current_request=MockRequest(json_body={'course_id': 'c343f71e-537c-45f0-9fce-e905720a28b9'}))
        result = get_info_by_id(app)
        expected_result = {
            "course": {
                "id": "c343f71e-537c-45f0-9fce-e905720a28b9",
                "course name": "Course A",
                "department id": "d44da5e5-f990-434a-887b-848f7a68bd3b",
                "semester": "2",
                "class": "Class A",
                "lecture hours": "4",
                "submitted by": "sam yake",
                "updated at": "2023-07-16T19:08:02.801165"
            }
        }

        self.assertEqual(result, expected_result)

    def test_get_info_by_id_non_existing_courses(self):
        # Test the case where the course does not exist in the database
        app = MockApp(current_request=MockRequest(json_body={'course_id': 'b10c5848-ce30-40dd-a09c-2e1b837c1a39'}))
        result = get_info_by_id(app)
        expected_result = {'message': 'course not found'}
        self.assertEqual(result, expected_result)

    def test_patch_courses(self):
        # Test the case where we patch course in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_courses': "2a6a6141-1992-4c54-85fd-d2d161e16668", "lecture_hours": "rosie"}))
        result = patch_courses(app)
        expected_result = {'message': 'Patched successfully'}
        self.assertEqual(result, expected_result)

    def test_put_courses(self):
        # Test the case where we put course in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_courses': "061cf2d2-2f71-11ee-be56-0242ac120002", "course_name": "Course A",
                       "department_id_course": "b10c5848-ce30-40dd-a09c-2e1b837c1a39", "semester": "Class A", "class_course": "blue", "lecture_hours": "beam",
                       "submitted_by_courses": "Alaska"}))

        result = put_courses(app)
        expected_result = {'message': ' Updated successfully'}
        self.assertEqual(result, expected_result)

    def test_post_courses(self):
        # Test the case where we post course in the database
        app = MockApp(current_request=MockRequest(
            json_body={'id_courses': "061cf2d2-2f71-11ee-be56-0242ac120002", "course_name": "Course A",
                       "department_id_course": "d44da5e5-f990-434a-887b-848f7a68bd3b", "semester": "Class A", "class_course": "blue", "lecture_hours": "beam",
                       "submitted_by_courses": "Alaska"}))
        result = post_courses(app)
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
