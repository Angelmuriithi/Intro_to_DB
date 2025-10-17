import pymysql
from pymysql import err

def create_database():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='k.a.g.w.i.r.i.a',  
            charset='utf8mb4',
            cursorclass=pymysql.cursors.Cursor
        )

        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            print("Database 'alxbookstore' created successfully!")

    except err.OperationalError as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

if __name__ == '__main__':
    create_database()
