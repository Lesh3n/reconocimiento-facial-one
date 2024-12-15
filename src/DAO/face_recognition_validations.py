#import DAO.connection as connection
from DAO.connection import get_db_connection

cursor, conn = get_db_connection()
if not conn:
    raise Exception("There's no connection with the database. Quitting...")

def try_db():
    try:
        print('hola')
        query = 'SELECT "Hello World!"'
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(f"Some error occurred: {e}")


def recuperar_clientes():
    try:
        query = 'SELECT * FROM clientes'
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Some error occurred: {e}")


if __name__ == '__main__':
    #try_db() #This tries the connection to the db, if it connects then it says hello world.
    recuperar_clientes()