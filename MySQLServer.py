import mysql.connector  
import pymysql

def create_database():
    connection = None
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='k.a.g.w.i.r.i.a',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.Cursor
        )

        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection and connection.open:
            connection.close()

if __name__ == '__main__':
    create_database()
