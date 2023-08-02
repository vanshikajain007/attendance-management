from database.db import get_db_connection
import uuid
import logging


# this function patches data
def patch_department(departments_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = departments_app.current_request.json_body
    try:
        id_departments = data.get('id_departments')
        submitted_by_departments = data.get('submitted_by_departments')
        update_query_departments = """
                                        UPDATE departments
                                        SET submitted_by = %s
                                        WHERE id = %s
                                    """
        cursor.execute(update_query_departments, (submitted_by_departments, id_departments))
        conn.commit()

        logging.info('department updated')
        return {'message': ' updated successfully'}

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function puts data
def put_department(departments_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = departments_app.current_request.json_body

    try:
        department_name = data.get('department_name')
        id_departments = data.get('id_departments')
        submitted_by_departments = data.get('submitted_by_departments')

        update_query_departments = """
                                        UPDATE departments
                                        SET submitted_by = %s,
                                        department_name = %s
                                        WHERE id = %s
                """

        cursor.execute(update_query_departments, (submitted_by_departments, department_name, id_departments))
        conn.commit()

        logging.info('department updated')

        return {'message': 'Updated successfully'}

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function posts data
def post_department(departments_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = departments_app.current_request.json_body

    try:
        department_name = data.get('department_name')
        department_id = str(uuid.uuid4())
        submitted_by_departments = data.get('submitted_by')
        insert_query_departments = "INSERT INTO departments (id, department_name, submitted_by, updated_at) " \
                                   "VALUES (%s ,%s, %s,  NOW())"

        values_students = (department_id, department_name, submitted_by_departments,)

        cursor.execute(insert_query_departments, values_students)
        conn.commit()

        logging.info('department posted')
        return {'message': ' Posted successfully'}

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# this function is used to get information from the table.
def get_info_by_id(departments_app):
    conn = get_db_connection()
    cursor = conn.cursor()

    # accessing data from request body
    data = departments_app.current_request.json_body

    # student id is taken as input
    department_id = data.get('department_id')
    try:
        select_query_department = "SELECT * FROM departments WHERE id = %s"
        values_department = (department_id,)

        cursor.execute(select_query_department, values_department)

        # Fetch the result of the query
        department_data = cursor.fetchone()

        if department_data:

            # Convert datetime objects to string before returning
            processed_data = {
                'department': {
                    'id': department_data[0],
                    'department name': department_data[1],
                    'submitted by': department_data[2],
                    'updated at': department_data[3].isoformat()

                    # Convert other datetime fields as needed
                }
            }
            logging.info('department data')
            return processed_data
        else:
            logging.info('department data not found')
            return {'message': 'department not found'}

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return {'error': str(e)}
    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

