from db import get_db_connection
import uuid
import logging
import psycopg2


# this function deletes row of a table.
def soft_delete_students(students_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = students_app.current_request.json_body

    try:
        # Prepare the DELETE query
        student_id = data.get('student_id')

        update_query = "UPDATE students SET deleted = TRUE WHERE id = %s"
        cursor.execute(update_query, (student_id,))

        conn.commit()
        logging.info(f"Student with ID {student_id} has been soft deleted.")

        return f"Student with ID {student_id} has been deleted."

    except psycopg2.Error as e:
        error_message = str(e)
        logging.error(error_message)
        # Handle the exception appropriately
        return {'error': error_message}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def patch_students(students_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = students_app.current_request.json_body

    try:
        id_students = data.get('id_students')
        full_name_students = data.get('full_name_students')
        department_id_students = data.get('department_id_students')
        class_students = data.get('class_students')
        submitted_by_students = data.get('submitted_by_students')
        token_students = data.get('token_students')

        update_query_students = """
                                        UPDATE students
                                        SET full_name = %s
                                        WHERE id = %s
                                        
                                    """
        cursor.execute(update_query_students, (full_name_students, id_students))
        conn.commit()

        return {'message': ' updated successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def put_students(students_app):
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    data = students_app.current_request.json_body

    try:
        id_students = data.get('id_students')
        full_name_students = data.get('full_name_students')
        department_id_students = data.get('department_id_students')
        class_students = data.get('class_students')
        submitted_by_students = data.get('submitted_by_students')

        update_query_students = """
            UPDATE students
            SET full_name = %s,
                department_id = %s,
                class = %s,
                submitted_by = %s
            WHERE id = %s
        """

        # Use a tuple to pass parameters to the cursor.execute() method
        values_students = (
            full_name_students,
            str(department_id_students),  # Convert UUID to string
            class_students,
            submitted_by_students,
            id_students
        )

        cursor.execute(update_query_students, values_students)
        conn.commit()

        return {'message': 'Updated successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
# this function deletes row of a table.
def post_students(students_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = students_app.current_request.json_body

    try:
        student_id = str(uuid.uuid4())
        full_name_student = data.get('full_name_student')
        department_id_student = data.get('department_id_student')
        class_student = data.get('class_student')
        submitted_by_student = data.get('submitted_by_student')
        insert_query_students = "INSERT INTO students (id, full_name, department_id , class, submitted_by, updated_at) " \
                                "VALUES (%s ,%s, %s, %s ,%s, NOW())"

        values_students = (student_id, full_name_student, department_id_student, class_student, submitted_by_student,)

        cursor.execute(insert_query_students, values_students)
        conn.commit()

        return {'message': ' Posted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


def get_info_by_id(students_app):
    conn = get_db_connection()
    cursor = conn.cursor()

    # accessing data from request body
    data = students_app.current_request.json_body

    # student id is taken as input
    student_id = data.get('student_id')
    try:

        select_query_students = "SELECT * FROM students WHERE id = %s"
        values_students = (student_id,)

        cursor.execute(select_query_students, values_students)

        # Fetch the result of the query
        student_data = cursor.fetchone()

        if student_data:
            # Convert datetime objects to string before returning
            processed_data = {
                'student': {
                    'id': student_data[0],
                    'full name': student_data[1],
                    'department id': student_data[2],
                    'class': student_data[3],
                    'submitted by': student_data[4],
                    'updated at': student_data[5].isoformat()

                }
            }

            logging.info("Data for student with ID %s retrieved successfully", student_id)

            return processed_data

        else:
            logging.warning("Student with ID %s not found", student_id)
            return {'message': 'Student not found'}

    except Exception as e:
        logging.error("An error occurred: %s", str(e))

        return {'error': str(e)}
    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()


def get_active_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        select_query = "SELECT * FROM students WHERE deleted = FALSE"
        cursor.execute(select_query)
        active_students = cursor.fetchall()
        print(active_students)
        student_list = []
        if active_students:
            print(type(active_students))
            # Convert datetime objects to string before returning
            for i in active_students:
                student_list.append({
                    'student': {
                        'id': i[0],
                        'full name': i[1],
                        'department id': i[2],
                        'class': i[3],
                        'submitted by': i[4],
                        'updated at': str(i[5])
                    }
                })

        return student_list
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
        conn.close()


def get_non_active_students(students_app):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        select_query = "SELECT * FROM students WHERE deleted = TRUE"
        cursor.execute(select_query)
        active_students = cursor.fetchall()
        student_list = []
        if active_students:
            # Convert datetime objects to string before returning
            for i in active_students:
                student_list.append({
                    'student': {
                        'id': i[0],
                        'full name': i[1],
                        'department id': i[2],
                        'class': i[3],
                        'submitted by': i[4],
                        'updated at': str(i[5])
                    }
                })

        return student_list
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
        conn.close()


def present_students(students_app):
    conn = get_db_connection()
    cursor = conn.cursor()
    present_attendance = str(1)
    select_query_attendance_log = """
                                       SELECT student_id FROM attendance_log
                                       WHERE present = %s
                                       """
    value_attendance_log = present_attendance
    cursor.execute(select_query_attendance_log, value_attendance_log)

    student_present_data = cursor.fetchall()
    return student_present_data




