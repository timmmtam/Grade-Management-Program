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
    if (flag == 0):
        input("\nPress ENTER to continue...")


def add_student():
    print("\n--------------------------------------")
    print("            Add a Student             ")
    print("--------------------------------------")
    while True:
        while True:
            student_id = input("Enter a new Student ID: ")
            if (student_id.isdigit() is False):
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
            if (all(chr.isalpha() or chr.isspace() for chr in student_name)):
                break
            else:
                print("Error. Student name must be contain alphabets only.")
                retry = input("Try again? (Y/N): ")
                if (retry.upper() == "Y"):
                    continue
                else:
                    return
        while True:
            student_email = input("Enter student's email: ")
            for student in student_list:
                if (student_email == student.email):
                    print(f"Error. Email already exists under {student.name}.")
                    print("Email must be unique.")
                    retry = input("Try again? (Y/N): ")
                    if (retry.upper() == "Y"):
                        break
                    else:
                        return
            else:
                break
        new_student = Student(student_id, student_name, student_email)
        student_list.append(new_student)
        with open("students.txt", "a") as f:
            f.write(f"{student_id},{student_name},{student_email}\n")
        print(f"Success! {student_name}({student_id}) is now a student.")
        retry = input("Do you want to add another student? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            return


def enroll_student():
    print("\n--------------------------------------")
    print("           Enroll a Student           ")
    print("--------------------------------------")
    while True:
        student_id = input("Select the Student ID to enroll into a course: ")
        if (student_id not in (stu.student_id for stu in student_list)):
            print("Error. Student does not exist.")
            return
        course_id = input("Select the Course ID to enroll the student in: ")
        if (course_id not in (course.course_id for course in course_list)):
            print("Error. Course does not exist.")
            return
        for student in student_list:
            if (student_id == student.student_id):
                for key in student.enrolled_courses:
                    if (key == course_id):
                        print("Error.")
                        print("Student is already enrolled in this course.")
                        return
                student.enrolled_course = {f"{course_id}": {}}
                print(f"Success! {student_id} is now enrolled in {course_id}.")
        #write to file here
        retry = print("Do you want to enroll another student? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            break


def record_marks():
    print("\n--------------------------------------")
    print("         Record Student Marks         ")
    print("--------------------------------------")
    display_students()
    student_id = input("Input Student ID to record marks: ")
    if student_id not in (student.student_id for student in student_list):
        print("Error. Student does not exist.")
        return
    print(f"Enrolled courses for {student_id}")
    print("------------------------------------")
    for student in student_list:
        if (student_id == student.student_id):
            for key in student.enrolled_courses:
                print(f"{key}")
    course_id = input("Input Course ID to record marks for: ")
    enrolled = any(course_id in (s.enrolled_courses for s in student_list))
    if (enrolled):
        while (True):
            marks = input(f"Enter marks for {student_id} in {course_id}: ")
            try:
                float(marks)
                break
            except ValueError:
                print("Error. The input must be a number.")
                retry = input("Try again? (Y/N): ")
                if (retry.upper() == "Y"):
                    continue
                else:
                    return
        student.enrolled_courses[f"{course_id}"] = {"Marks": f"{marks:.2f}"}


def manage_students():
    go_back = False

    while (go_back is not True):
        print("\n--------------------------------------")
        print("          Managing Students           ")
        print("--------------------------------------")
        print("""[1] Display student list
[2] Add a student
[3] Enroll a Student
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
                enroll_student()
            case "4":
                record_marks()
            case "5":
                display_student_performance()
            case "6":
                export_student_performance()
            case "7":
                go_back = True
            case _:
                print("\nError. Input is not a number 1-7. Please try again.")
                input("Press ENTER to continue...")
