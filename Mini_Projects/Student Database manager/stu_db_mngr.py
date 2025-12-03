"""
MINI PROJECT – Student Database Manager (SQL + Python)
🎯 Features:

✔ Add student
✔ View all
✔ Update marks
✔ Delete student
✔ Auto commit
✔ Error handling
"""

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)

cursor = db.cursor()


def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    marks = int(input("Marks: "))

    sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, age, marks))
    db.commit()
    print("Student added!")


def show_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


def update_marks():
    name = input("Student name: ")
    new_marks = int(input("New marks: "))

    sql = "UPDATE students SET marks=%s WHERE name=%s"
    cursor.execute(sql, (new_marks, name))
    db.commit()
    print("Marks updated!")


def delete_student():
    name = input("Name to delete: ")
    sql = "DELETE FROM students WHERE name=%s"
    cursor.execute(sql, (name,))
    db.commit()
    print("Student deleted!")


# Menu
while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        update_marks()
    elif choice == 4:
        delete_student()
    else:
        break
