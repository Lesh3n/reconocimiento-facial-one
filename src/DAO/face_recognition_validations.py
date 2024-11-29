import connection

cursor, conn = connection.get_db_connection()
if not conn:
    raise Exception("There's no connection with the database. Quitting...")

def try_db():
    print('hola')
    query = 'SELECT "Hello World!"'
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)


if __name__ == '__main__':
    try_db()