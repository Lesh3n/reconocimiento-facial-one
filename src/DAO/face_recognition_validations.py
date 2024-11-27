from . import connection
import pymysql.cursors

def try_db():
    with connection:
        with connection.cursor() as cursor:
            query = 'SELECT "Hello World!'
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            cursor.close()
    
    connection.close()


if '__name__' == '__main__':
    try_db()