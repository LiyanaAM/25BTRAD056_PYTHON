while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        f = open("students.txt", "a")
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        f.write(name + "," + roll + "\n")
        f.close()
        print("Record added")

    elif choice == "2":
        f = open("students.txt", "r")
        print(f.read())
        f.close()

    elif choice == "3":
        search = input("Enter roll number: ")
        f = open("students.txt", "r")
        found = False

        for line in f:
            if search == line.strip().split(",")[1]:
                print(line)
                found = True

        f.close()

        if not found:
            print("Student not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
