#Create Table Student

from database import get_connection

def create_student_table():
    db = get_connection()
    if db is None:
        return
    
    cursor = db.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        grade VARCHAR(10)
    );
    """
    
    try:
        cursor.execute(create_table_query)
        db.commit()
        print("Table 'students' is ready.")
    except Exception as e:
        print("Error while creating table:", e)
    finally:
        cursor.close()
        db.close()
        
if __name__ == "__main__":
    create_student_table()