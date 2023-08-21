import psycopg2


# database connection
get_db_connection = lambda: psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)

db_host = 'localhost'
db_name = 'postgres'
db_user = 'postgres'
db_password = ''
db_port = '5432'
