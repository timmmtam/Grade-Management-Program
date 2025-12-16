# Module for managing students
from .config import student_list, course_list
from .classes import Student


def display_students(flag):
    # Display the list of students with their student_id
    print("\n--------------------------------------")
    print("             Student List             ")
    print("--------------------------------------")
    for student in student_list:
        print(student)
    if (flag == 0)
        input("\nPress ENTER to continue...")


def add_student():
    print("\n--------------------------------------")
    print("            Add a Student             ")
    print("--------------------------------------")
    while True:
        while True:
            student_id = input("Enter a new Student ID: ")
            if (student_id.isdigit() == False):
                print("Error. Student ID must contain numbers only.")
                retry = input("Try again? (Y/N): ")
                if (retry.upper() == "Y"):
                    continue
                else:
                    return
            else:
                break
        for student in student_list:
            if (student_id == student.student_id):
                print("Error. Student already exists.")
                return
        while True:
            student_name = input("Enter the student's name: ")
            if (student_name.isalpha() == False):
                print("Error. Student name must be contain alphabets only.")
                retry = input("Try again? (Y/N): ")
                if (retry.upper() == "Y"):
                    continue
                else:
                    return
            else:
                break
        student_email = input("Enter student's email: ")
        new_student = Student(student_id, student_name, student_email)
        student_list.append(new_student)
        with open("students.txt", "a") as f:
            f.write(f"{student_id},{student_name},{student_email}\n")
        print(f"Complete! Student {student_name}({student_id}) has been successfully added to the system.")
        retry = input("Do you want to add another student? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            return


def remove_student():
    print("\n--------------------------------------")
    print("          Remove a Student           ")
    print("--------------------------------------")
    display_students(1)
    student_id = input("Enter Student ID to remove: ")
    for i in range(len(student_list) - 1, -1, -1):
        if (student_list[i].student_id == student_id):
            student_list.pop(i)



def manage_students():
    go_back = False

    while (go_back is not True):
        print("\n--------------------------------------")
        print("          Managing Students           ")
        print("--------------------------------------")
        print("""[1] Display student list
[2] Add a student
[3] Remove a student
[4] Record marks
[5] Display student performance
[6] Export student performance
[7] Go back""")

        # Input from user
        option = input("\nPlease select [1-7]: ")

        match option:
            case "1":
                display_students(0)
            case "2":
                add_student()
            case "3":
                remove_student()
            case "4":
                record_marks()
            case "5":
                display_student_performance()
            case "6":
                export_student_performance()
            case "7":
                go_back = True
            case _:
                print("\nError. Input is not a number 1-6. Please try again.")
                input("Press ENTER to continue...")
