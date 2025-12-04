def add_log(message):
    with open("Mini_Projects/Log Management/app.log", "a") as f:
        f.write(message + "\n")

def read_logs():
    with open("Mini_Projects/Log Management/app.log", "r") as f:
        print(f.read())

def clear_logs():
    with open("Mini_Projects/Log Management/app.log", "w") as f:
        f.write("")  # empty file

while True:
    print("\n1. Add Log\n2. Read Logs\n3. Clear Logs\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        msg = input("Enter log message: ")
        add_log(msg)

    elif choice == 2:
        read_logs()

    elif choice == 3:
        clear_logs()

    elif choice == 4:
        break

    else:
        print("Invalid choice!")
