from app.db import get_db_connection
import psycopg2
import logging


# this function creates table.
def create_table(app):
    conn = get_db_connection()

    cursor = conn.cursor()

    try:
        create_table_query_users = '''
                CREATE TABLE users (
                    id UUID PRIMARY KEY,
                    type VARCHAR,
                    full_name VARCHAR,
                    username VARCHAR,
                    email VARCHAR,
                    password VARCHAR,
                    submitted_by VARCHAR,
                    updated_at TIMESTAMP,
                    token VARCHAR

                );
        '''

        cursor.execute(create_table_query_users)

        create_table_query_department = '''
             CREATE TABLE departments (
             id UUID PRIMARY KEY,
             department_name VARCHAR,
             submitted_by VARCHAR,
             updated_at TIMESTAMP NOT NULL


             );
         '''

        cursor.execute(create_table_query_department)

        create_table_query_courses = '''
                 CREATE TABLE courses(
                 id UUID PRIMARY KEY,
                 course_name VARCHAR,
                 department_id UUID,
                 semester VARCHAR,
                 class VARCHAR,
                 lecture_hours VARCHAR,
                 submitted_by VARCHAR,
                 updated_at TIMESTAMP ,
                 FOREIGN KEY (department_id) REFERENCES departments (id)

                 );
        '''

        cursor.execute(create_table_query_courses)

        create_table_query_attendance_log = '''
                     CREATE TABLE attendance_log (
                     id UUID PRIMARY KEY,
                     student_id UUID,
                     course_id UUID,
                     present BOOLEAN,
                     submitted_by UUID,
                     updated_at TIMESTAMP ,
                     FOREIGN KEY (student_id) REFERENCES students (id) ,
                     FOREIGN KEY (course_id) REFERENCES courses (id),
                     FOREIGN KEY (submitted_by) REFERENCES users (id)


                     );
        '''

        cursor.execute(create_table_query_attendance_log)

        create_table_query_students = '''
                CREATE TABLE students (
                    id UUID PRIMARY KEY,
                    full_name VARCHAR,
                    department_id UUID,
                    class VARCHAR,
                    submitted_by VARCHAR,
                    updated_at TIMESTAMP ,
                    password VARCHAR,
                    token VARCHAR,
                    FOREIGN KEY (department_id) REFERENCES departments (id)


                );
        '''

        cursor.execute(create_table_query_students)
        logging.info("Table 'users' created successfully.")

        conn.commit()

        return {'message': 'Table created successfully.'}


    except psycopg2.Error as e:

        error_message = str(e)

        logging.error(error_message)

        # Handle the exception appropriately

        return {'error': error_message}

    # Close the database connection
    finally:
        cursor.close()
        conn.close()


# create function is called here
if __name__ == "__main__":
    create_table()
