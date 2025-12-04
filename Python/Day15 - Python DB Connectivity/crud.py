from database import get_connection

def insert_student(name, age, grade):
    db = get_connection()
    if db is None:
        return
    
    cursor = db.cursor()
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    
    try:
        cursor.execute(query, values)
        db.commit()
        print(f"Student inserted with id = {cursor.lastrowid}")
    except Exception as e:
        print("Error while inserting student:", e)
    finally:
        cursor.close()
        db.close()
        

def get_all_students():
    db = get_connection()
    if db is None:
        return
    
    cursor = db.cursor()
    query = "SELECT id, name, age, grade FROM students"
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("No students Found.")
            return
        
        print("\n All Students:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    except Exception as e:
        print("Error while reading students:", e)
    finally:
        cursor.close()
        db.close()
        

def get_student_by_id(student_id):
    db = get_connection()
    if db is None:
        return
    
    cursor = db.cursor()
    query = "SELECT id, name, age, grade FROM students WHERE id = %s"
    
    try:
        cursor.execute(query, (student_id,))
        row = cursor.fetchone()
        if row:
            print(f" Student Found -> ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
        else:
            print("No student found with that ID.")
    except Exception as e:
        print("Error while reading student:", e)
    finally:
        cursor.close()
        db.close()
        

def update_student(student_id, name, age, grade):
    db = get_connection()
    if db is None:
        return

    cursor = db.cursor()
    query = """
    UPDATE students
    SET name = %s, age = %s, grade = %s
    WHERE id = %s
    """
    values = (name, age, grade, student_id)

    try:
        cursor.execute(query, values)
        db.commit()
        if cursor.rowcount > 0:
            print(f"✅ Student with ID {student_id} updated.")
        else:
            print("⚠️ No student found to update.")
    except Exception as e:
        print("❌ Error while updating student:", e)
    finally:
        cursor.close()
        db.close()



def delete_student(student_id):
    db = get_connection()
    if db is None:
        return

    cursor = db.cursor()
    query = "DELETE FROM students WHERE id = %s"

    try:
        cursor.execute(query, (student_id,))
        db.commit()
        if cursor.rowcount > 0:
            print(f"🗑️ Student with ID {student_id} deleted.")
        else:
            print("⚠️ No student found to delete.")
    except Exception as e:
        print("❌ Error while deleting student:", e)
    finally:
        cursor.close()
        db.close()
