from db import get_db_connection
import uuid


secret_key_final = 'alaska'


def soft_delete_users(users_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = users_app.current_request.json_body

    try:
        # Prepare the DELETE query
        user_id = data.get('user_id')

        update_query = "UPDATE users SET deleted = TRUE WHERE id = %s"
        cursor.execute(update_query, (user_id,))

        conn.commit()

        a = f"user with ID {user_id} has been deleted."
        return a

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


def patch_users(users_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = users_app.current_request.json_body

    try:
        id_user = data.get('id_user')
        type_user = data.get('type_user')
        full_name_user = data.get('full_name_user')
        username = data.get('username')
        email = data.get('email')
        password_user = data.get('password_user')
        submitted_by_user = data.get('submitted_by_user')

        update_query_user = """
                                               UPDATE users
                                               SET type = %s
                                               WHERE id = %s
                                           """
        cursor.execute(update_query_user, (type_user, id_user))
        conn.commit()

        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


def put_users(users_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = users_app.current_request.json_body

    try:
        id_user = data.get('id_user')
        type_user = data.get('type_user')
        full_name_user = data.get('full_name_user')
        username = data.get('username')
        email = data.get('email')
        password_user = data.get('password_user')
        submitted_by_user = data.get('submitted_by_user')

        update_query_users = """
                                                UPDATE users
                                                SET type = %s
                                                full_name = %s
                                                username = %s
                                                email = %s
                                                password = %s
                                                submitted_by = %s
                                                WHERE id = %s
                                            """
        cursor.execute(update_query_users,(type_user, full_name_user, username, email, password_user, submitted_by_user, id_user))
        conn.commit()

        return {'message': ' Deleted successfully'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        conn.close()
        cursor.close()


# @authenticate
def post_users(users_app):
    # Connect to the database
    conn = get_db_connection()

    cursor = conn.cursor()

    data = users_app.current_request.json_body

    try:
        users_id = str(uuid.uuid4())
        type_of_user = data.get('type_of_user')
        full_name_user = data.get('full_name_user')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        submitted_by = data.get('submitted_by')
        insert_query_users = "INSERT INTO users (id, type, full_name, username, email, password, submitted_by, updated_at) " \
                             "VALUES (%s ,%s, %s, %s ,%s, %s, %s, NOW())"

        values_users = (users_id, type_of_user, full_name_user, username, email, password, submitted_by,)

        cursor.execute(insert_query_users, values_users)
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
def get_info_by_id(users_app):
    conn = get_db_connection()
    cursor = conn.cursor()

    # accessing data from request body
    data = users_app.current_request.json_body

    # student id is taken as input
    users_id = data.get('users_id')
    try:
        select_query_users = "SELECT * FROM users WHERE id = %s"
        values_users = (users_id,)

        cursor.execute(select_query_users, values_users)

        # Fetch the result of the query
        users_data = cursor.fetchone()

        if users_data:
            # Process the student data as needed
            # ...

            # Convert datetime objects to string before returning
            processed_data = {
                'user': {
                    'Id': users_data[0],
                    'Type': users_data[1],
                    'Full name': users_data[2],
                    'Username': users_data[3],
                    'Email-id': users_data[4],
                    'submitted by': users_data[6],
                    'updated at': users_data[7].isoformat()

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


def get_active_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        select_query = "SELECT * FROM users WHERE deleted = FALSE"
        cursor.execute(select_query)
        active_users = cursor.fetchall()
        print(active_users)
        User_list = []
        if active_users:
            print(type(active_users))
            # Convert datetime objects to string before returning
            for i in active_users:
                User_list.append({
                    'student': {
                        'id': i[0],
                        'full name': i[1],
                        'department id': i[2],
                        'class': i[3],
                        'submitted by': i[4],
                        'updated at': str(i[5])
                    }
                })

        return User_list
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
        conn.close()


def get_non_active_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        select_query = "SELECT * FROM students WHERE deleted = TRUE"
        cursor.execute(select_query)
        active_users = cursor.fetchall()
        print(active_users)
        User_list = []
        if active_users:
            print(type(active_users))
            # Convert datetime objects to string before returning
            for i in active_users:
                User_list.append({
                    'student': {
                        'id': i[0],
                        'full name': i[1],
                        'department id': i[2],
                        'class': i[3],
                        'submitted by': i[4],
                        'updated at': str(i[5])
                    }
                })

        return User_list
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
        conn.close()


