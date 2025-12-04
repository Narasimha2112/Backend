class Student:
    def __init__(self, name, marks):
        self.name = name              # student name
        self.marks = marks            # list of marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def display(self):
        print(f"\nStudent: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average()}")


students = []  # store all student objects

# Menu driven program
while True:
    print("\n1. Add Student\n2. Show All Students\n3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        
        marks = []
        for i in range(3):
            m = int(input(f"Enter mark {i+1}: "))
            marks.append(m)

        s = Student(name, marks)
        students.append(s)

    elif choice == 2:
        for s in students:
            s.display()

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
