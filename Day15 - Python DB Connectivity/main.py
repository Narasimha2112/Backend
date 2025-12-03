# main.py
from table_creation import create_student_table
from crud import (
    insert_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
)


def main():
    print("🔧 Setting up table...")
    create_student_table()

    print("\n➕ Inserting students...")
    insert_student("Rahul", 20, "10th")
    insert_student("Sneha", 18, "12th")

    print("\n📖 Fetching all students...")
    get_all_students()

    print("\n🔍 Fetching student with ID = 1")
    get_student_by_id(1)

    print("\n✏️ Updating student with ID = 1")
    update_student(1, "Rahul Kumar", 21, "BSc")

    print("\n📖 Fetching all students after update...")
    get_all_students()

    print("\n🗑️ Deleting student with ID = 2")
    delete_student(2)

    print("\n📖 Fetching all students after delete...")
    get_all_students()

if __name__ == "__main__":
    main()
