import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

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