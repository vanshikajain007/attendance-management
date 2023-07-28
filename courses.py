from chalice import Chalice, UnauthorizedError
# from authenticate import authenticate
from db import get_db_connection
import uuid


# from app import app

# app = Chalice(app_name='Attendance management system-chalice')


# @authenticate
# this function deletes row of a table.
def delete_courses(courses_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = courses_app.current_request.json_body

    try:
        # Prepare the DELETE query
        courses_id = data.get('log_id')
        delete_query_courses = """
                                               DELETE FROM courses
                                               WHERE id = %s
                                           """
        cursor.execute(delete_query_courses, (courses_id,))
        conn.commit()

        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def patch_courses(courses_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = courses_app.current_request.json_body

    try:
        id_courses = data.get('id_courses')
        course_name = data.get('course_name')
        department_id_course = data.get('department_id_course')
        semester = data.get('semester')
        class_courses = data.get('class_courses')
        lecture_hours = data.get('lecture_hours')
        submitted_by_courses = data.get('submitted_by_courses')

        update_query_courses = """
                                                    UPDATE courses
                                                    SET lecture_hours = %s
                                                    WHERE id = %s
                                                """
        cursor.execute(update_query_courses, (lecture_hours, id_courses))
        conn.commit()

        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def put_courses(courses_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = courses_app.current_request.json_body

    try:
        id_courses = data.get('id_courses')
        course_name = data.get('course_name')
        department_id_course = data.get('department_id_course')
        semester = data.get('semester')
        class_courses = data.get('class_courses')
        lecture_hours = data.get('lecture_hours')
        submitted_by_courses = data.get('submitted_by_courses')

        update_query_courses = """
                                                   UPDATE courses
                                                   SET course_name = %s
                                                   department_id = %s
                                                   semester = %s
                                                   class = %s
                                                   lecture_hours = %s
                                                   submitted_by = %s
                                                   WHERE id = %s
                                               """
        cursor.execute(update_query_courses, (lecture_hours, course_name, department_id_course, semester, class_courses, submitted_by_courses, id_courses))

        conn.commit()
        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def post_courses(courses_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = courses_app.current_request.json_body

    try:
        course_id_courses = str(uuid.uuid4())
        course_name = data.get('course_name')
        department_id_course = data.get('department_id_course')
        semester = data.get('semester')
        class_course = data.get('class_course')
        lecture_hours = data.get('lecture_hours')
        submitted_by_course = data.get('submitted_by_course')
        insert_query_courses = "INSERT INTO courses (id, course_name,  department_id, semester, class, lecture_hours, submitted_by, updated_at) " \
                               "VALUES (%s ,%s, %s, %s ,%s, %s, %s, NOW())"

        values_courses = (course_id_courses, course_name, department_id_course, semester, class_course, lecture_hours,
                          submitted_by_course,)

        cursor.execute(insert_query_courses, values_courses)
        conn.commit()

        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# authenticate function is called to protect the api.
# @authenticate
# this function is used to get information from the table.
def get_info_by_id(courses_app):
    conn = get_db_connection()
    cursor = conn.cursor()

    # accessing data from request body
    data = courses_app.current_request.json_body

    # student id is taken as input
    course_id = data.get('course_id')
    try:
        select_query_courses = "SELECT * FROM courses WHERE id = %s"
        values_courses = (course_id,)

        cursor.execute(select_query_courses, values_courses)

        # Fetch the result of the query
        course_data = cursor.fetchone()

        if course_data:
            # Convert datetime objects to string before returning
            processed_data = {
                'course': {
                    'id': course_data[0],
                    'course name': course_data[1],
                    'department id': course_data[2],
                    'semester': course_data[3],
                    'class': course_data[4],
                    'lecture hours': course_data[5],
                    'submitted by': course_data[6],
                    'updated at': course_data[7].isoformat()

                    # Convert other datetime fields as needed
                }
            }

            return processed_data
        else:
            return {'message': 'course not found'}

    except Exception as e:

        return {'error': str(e)}
    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
