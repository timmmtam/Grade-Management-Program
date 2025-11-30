# Module for managing students
from .config import student_list, course_list


def display_students():
    # Display the list of students with their student_id
    print("\n--------------------------------------")
    print("             Student List             ")
    print("--------------------------------------")
    for student in student_list:
        print(student)
    input("\nPress ENTER to continue...")

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
                display_students()
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
