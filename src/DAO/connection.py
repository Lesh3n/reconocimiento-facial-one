import pymysql
import os
from dotenv import load_dotenv

is_production : bool = False

load_dotenv()
match is_production:
    case True:
        print('production mode!!')
        def get_db_connection():
            conn = pymysql.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME'),
                port=3306
            )
            print('connected!')
            cursor = conn.cursor()
            print('cursor created!')
            return cursor, conn
    case _:
        print('development mode!!')
        def get_db_connection():
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='rootpassword',
                database='recofacial',
                port=3306
            )
            print('connected!')
            cursor = conn.cursor()
            print('cursor created!')
            return cursor, conn
