import uuid

from database.db import get_db_connection


# this function patches data
def patch_attendance_log(attendance_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = attendance_app.current_request.json_body

    try:
        id_log = data.get('id_log')
        student_id_log = data.get('student_id_log')
        course_id_log = data.get('course_id_log')
        present_log = data.get('present_log')
        submitted_by_log = data.get('submitted_by_log')

        update_query_attendance_log = """
                                            UPDATE attendance_log
                                            SET present = %s
                                            WHERE id = %s
                                        """
        cursor.execute(update_query_attendance_log, (present_log, id_log))
        conn.commit()

        return {'message': 'Updated successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function puts data
def put_attendance_log(attendance_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = attendance_app.current_request.json_body

    try:
        id_log = data.get('id_log')
        student_id_log = data.get('student_id_log')
        course_id_log = data.get('course_id_log')
        present_log = data.get('present_log')
        submitted_by_log = data.get('submitted_by_log')

        update_query_attendance_log = """
                                            UPDATE attendance_log
                                            SET present = %s,
                                            student_id = %s,
                                            course_id = %s,
                                            submitted_by = %s
                                            WHERE id = %s
                                        """
        cursor.execute(update_query_attendance_log,(present_log, student_id_log, course_id_log, submitted_by_log, id_log))
        conn.commit()

        return {'message': ' Updated successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function posts data
def post_attendance_log(attendance_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = attendance_app.current_request.json_body

    try:
        log_id = str(uuid.uuid4())
        student_id_attendance = data.get('student_id')
        course_id = data.get('course_id')
        present = data.get('present')
        submitted_by_log = data.get('submitted_by_log')
        # Insertion of values in attendance log table
        insert_query_attendance = "INSERT INTO attendance_log (id, student_id, course_id, present, submitted_by, updated_at) " \
                                  "VALUES (%s ,%s, %s, %s ,%s, NOW())"

        values_attendance = (log_id, student_id_attendance, course_id, present, submitted_by_log,)

        cursor.execute(insert_query_attendance, values_attendance)
        conn.commit()

        return {'message': ' Updated successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function is used to get information from the table.
def get_info_by_id(attendance_app):

    conn = get_db_connection()
    cursor = conn.cursor()

    # accessing data from request body
    data = attendance_app.current_request.json_body

    # student id is taken as input
    student_id = data.get('student_id')
    try:
        select_query_log = "SELECT * FROM attendance_log WHERE id = %s"
        values_log = (student_id,)

        cursor.execute(select_query_log, values_log)

        # Fetch the result of the query
        log_data = cursor.fetchone()

        if log_data:

            # Convert datetime objects to string before returning
            processed_data = {
                'log': {
                    'id': log_data[0],
                    'student id': log_data[1],
                    'course id': log_data[2],
                    'present': log_data[3],
                    'submitted by': log_data[4],
                    'updated at': log_data[5].isoformat()

                    # Convert other datetime fields as needed
                }
            }

            return processed_data
        else:
            return {'message': 'Student not found'}

    except Exception as e:

        return {'error': str(e)}
    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()




