import logging
from db import get_db_connection
import jwt
import uuid

secret_key_final = 'alaska'


# for new user
def sign_up(app):
    conn = get_db_connection()

    cursor = conn.cursor()

    data = app.current_request.json_body
    try:
        # getting information from user
        id_user = str(uuid.uuid4())
        type_of_user = data.get('type_of_user')
        full_name_user = data.get('full_name_user')
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        submitted_by = data.get('submitted_by')
        payload = {'email': email}

        secret_key = secret_key_final
        token_final = jwt.encode(payload, secret_key, algorithm='HS256')

        insert_query_users = "INSERT INTO users (id, type, full_name, username, email, password, submitted_by, token, deleted, updated_at) " \
                             "VALUES (%s ,%s, %s, %s ,%s, %s, %s, %s, %s, NOW())"

        values_users = (
            id_user, type_of_user, full_name_user, username, email, password, submitted_by, token_final, 'FALSE',)

        cursor.execute(insert_query_users, values_users)

        conn.commit()
        # logging.info('login successful')
        return "Sign up successful"

    except Exception as e:
        return "Sign up failed"

    finally:
        conn.close()
        cursor.close()


# for existing user
def login(app):
    conn = get_db_connection()

    cursor = conn.cursor()

    data = app.current_request.json_body
    try:
        # Getting email and password from the JSON body
        email = data.get('email')
        password = data.get('password')

        # Prepare the SQL query to select id and token based on email and password
        select_query_users = "SELECT id, token FROM users WHERE email = %s AND password = %s"
        values_users = (email, password)

        cursor.execute(select_query_users, values_users)

        # Fetch the result of the query
        user_data = cursor.fetchone()

        if user_data:
            # Convert the user_data tuple to a dictionary
            user_info = {
                'id': user_data[0],
                'token': user_data[1]
            }
            logging.info("Login for user with email-id %s successful", email)

            return user_info

        else:
            logging.error("user not found")
            return {'message': 'User not found'}

    except Exception as e:
        return {'error': str(e)}

    finally:
        cursor.close()
        conn.close()


# first user is made
# this will only be executed if first user doesn't exist
def setup(app):
    conn = get_db_connection()
    cursor = conn.cursor()
    first_user_username = 'user1'
    password = 'password@user1'
    email = 'firstuser@gmail.com'
    first_users_id = str(uuid.uuid4())
    first_user_type = 'first_user'
    payload = {'email': email}
    submitted_by_first_user = 'admin'
    secret_key = secret_key_final
    token_final = jwt.encode(payload, secret_key, algorithm='HS256')
    try:
        select_query_first_user = "SELECT * FROM users WHERE email = %s "
        params_first_user = (email,)
        cursor.execute(select_query_first_user, params_first_user)
        row = cursor.fetchone()

        if row is not None:  # Check if the row is not None
            full_name = row[2]
            if full_name == 'blake':
                return 'user exists'
            else:
                pass
        else:
            # The row is None, meaning no user with the provided email exists
            insert_query_first_user = "INSERT INTO users (id, type, full_name, username, email, password, submitted_by, token, deleted, updated_at) " \
                                      "VALUES (%s ,%s, %s, %s ,%s, %s, %s, %s, %s, NOW())"

            values_first_user = (first_users_id, first_user_type, "first user", first_user_username, email, password, submitted_by_first_user, token_final, 'FALSE',)

            cursor.execute(insert_query_first_user, values_first_user)

        conn.commit()
        return 'first user'
    finally:
        conn.close()
        cursor.close()
