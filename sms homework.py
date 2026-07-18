students = []


def add_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ")
    grade = float(input("Enter Student Grade: "))

    student = {
        "ID": student_id,
        "Name": name,
        "Grade": grade
    }

    students.append(student)
    print("Student added successfully.")


def show_all_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("---------------------------")
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Grade:", student["Grade"])


def search_student_by_id():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["ID"] == student_id:
            print("---------------------------")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Grade:", student["Grade"])
            return

    print("Student not found.")


def update_student_grade():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["ID"] == student_id:
            new_grade = float(input("Enter New Grade: "))
            student["Grade"] = new_grade
            print("Grade updated successfully.")
            return

    print("Student not found.")
    
def delete_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def calculate_average_grade():
    if len(students) == 0:
        print("No students found.")
        return

    total = 0

    for student in students:
        total += student["Grade"]

    average = total / len(students)

    print("Average Grade =", average)


def show_best_student():
    if len(students) == 0:
        print("No students found.")
        return

    best_student = students[0]

    for student in students:
        if student["Grade"] > best_student["Grade"]:
            best_student = student

    print("------ Best Student ------")
    print("ID:", best_student["ID"])
    print("Name:", best_student["Name"])
    print("Grade:", best_student["Grade"])


def show_worst_student():
    if len(students) == 0:
        print("No students found.")
        return

    worst_student = students[0]

    for student in students:
        if student["Grade"] < worst_student["Grade"]:
            worst_student = student

    print("------ Worst Student ------")
    print("ID:", worst_student["ID"])
    print("Name:", worst_student["Name"])
    print("Grade:", worst_student["Grade"])
    
def show_total_students():
    print("Total Students =", len(students))


def show_passed_students():
    if len(students) == 0:
        print("No students found.")
        return

    found = False

    print("------ Passed Students ------")

    for student in students:
        if student["Grade"] >= 60:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Grade:", student["Grade"])
            print("---------------------------")
            found = True

    if found == False:
        print("No passed students.")


def show_failed_students():
    if len(students) == 0:
        print("No students found.")
        return

    found = False

    print("------ Failed Students ------")

    for student in students:
        if student["Grade"] < 60:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Grade:", student["Grade"])
            print("---------------------------")
            found = True

    if found == False:
        print("No failed students.")
while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student by ID")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Calculate Average Grade")
    print("7. Show Best Student")
    print("8. Show Worst Student")
    print("9. Show Total Number of Students")
    print("10. Show Passed Students")
    print("11. Show Failed Students")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_all_students()

    elif choice == "3":
        search_student_by_id()

    elif choice == "4":
        update_student_grade()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average_grade()

    elif choice == "7":
        show_best_student()

    elif choice == "8":
        show_worst_student()

    elif choice == "9":
        show_total_students()

    elif choice == "10":
        show_passed_students()

    elif choice == "11":
        show_failed_students()

    elif choice == "12":
        print("Thank you for using the Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")                