# db_connection.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",      # where MySQL runs
            user="root",           # MySQL username
            password="Admin@123",  # 🔴 change this
            database="school"      # which DB to use
        )
        return connection
    except Error as e:
        print("❌ Error while connecting to MySQL:", e)
        return None
