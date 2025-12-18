#  Module for managing students
from .config import student_list, course_list
from .classes import Student
from .utils import grade_calculation


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
        print("\nStudent list\n---------------------")
        for student in student_list:
            print(student)

        student_id = input("\nSelect the Student ID to enroll into a course: ")
        if (student_id not in (stu.student_id for stu in student_list)):
            print("\nError. Student does not exist.")
            input("\nPress ENTER to continue...")
            return

        print("\nCourse list\n---------------------")
        for course in course_list:
            print(course)

        course_id = input("\nSelect the Course ID to enroll the student in: ")
        if (course_id not in (course.course_id for course in course_list)):
            print("\nError. Course does not exist.")
            input("\nPress ENTER to continue...")
            return
        for student in student_list:
            if (student_id == student.student_id):
                for key in student.enrolled_courses:
                    if (key == course_id):
                        print("\nError.")
                        print("Student is already enrolled in this course.")
                        input("\nPress ENTER to continue...")
                        return
                student.enrolled_courses[f"{course_id}"] = {}
                with open("grades.txt", "a") as f:
                    f.write(f"{student_id},{course_id}\n")
                print(f"\nSuccess! {student_id} is now enrolled in {course_id}.")

        retry = input("Do you want to enroll another student? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            break


def record_marks():
    print("\n--------------------------------------")
    print("         Record Student Marks         ")
    print("--------------------------------------")
    while True:
        print("\nStudent list\n---------------------")
        for student in student_list:
            print(student)
        print()

        student_id = input("Input Student ID to record marks: ")
        if student_id not in (student.student_id for student in student_list):
            print("\nError. Student does not exist.")
            input("\nPress ENTER... to continue")
            continue

        print(f"\nEnrolled courses for {student_id}")
        print("------------------------------------")
        for student in student_list:
            if (student_id == student.student_id):
                for key in student.enrolled_courses:
                    print(f"{key}")

        course_id = input("\nInput Course ID to record marks for: ")
        enrolled = any(course_id in s.enrolled_courses for s in student_list)
        if (enrolled):
            while (True):
                marks = input(f"Enter marks for {student_id} in {course_id}: ")
                try:
                    marks = round(float(marks), 2)
                    break
                except ValueError:
                    print("Error. The input must be a number.")
                    retry = input("Try again? (Y/N): ")
                    if (retry.upper() == "Y"):
                        continue
                    else:
                        return
            grade, gpa = grade_calculation(marks)
            marks = str(marks)
            for student in student_list:
                if (student_id == student.student_id):
                    student.enrolled_courses[f"{course_id}"] = {
                            "mark": marks,
                            "grade": grade,
                            "gpa": gpa}
            with open("grades.txt", "r") as f:
                lines = f.readlines()
            with open("grades.txt", "w") as f:
                for line in lines:
                    if (student_id in line and course_id in line):
                        parts = line.strip().split(",")
                        if (len(parts) > 2):
                            parts[2] = marks
                            parts[3] = grade
                            parts[4] = gpa
                            line = ",".join(parts) + "\n"
                        else:
                            line = ",".join(parts) + "," + marks + ","
                            line = line + grade + "," + gpa + "\n"
                    f.write(line)
            print(f"{student_id} has been graded {grade} in {course_id}.")
        else:
            print("\nError. Student in not enrolled in this course.")
        retry = input("\nRecord marks again? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            break


def display_student_performance():
    # Check data of students availability
    if len(student_list) == 0:
        print("Error: No data of students available!")
        input("Press ENTER to continue...")
        return # return back to module for managing students
    
    # Check data of courses availability
    if len(course_list) == 0:
        print("Error: No data of courses available!")
        input("Press ENTER to continue...")
        return # return back to module for managing students

    while True:
        print("\n--------------------------------------")
        print("      Display Student Performance     ")
        print("--------------------------------------")
        print("\nStudent list\n---------------------")
        for student in student_list:
            print(student)
        print()
        check_student_id = input("\nEnter Student ID to display performance: ")

        found = False
        for student in student_list:
            # The student id inputed exist in the list of student id
            if student.student_id == check_student_id: 
                found = True
                print(f"\nStudent: {student.name} ({student.student_id})")
                print(f"Email:{student.email}")
                print("-" * 50)

                # Table header with :<12 mean left-justified width of 12 characters
                print(f"{'Course ID':<12} {'Mark':<8}{'Grade':<8}{'GPA':<6}")

                # Loop through each enrolled course for the specific student
                for course_id, data in student.enrolled_courses.items():
                    mark = data.get("mark", "0") # Get the mark's data, safely return 0 when not have mark's data
                    grade = data.get("grade", "N/A") # Get the grade's data, safely return Not Recorded when not have grade's data
                    gpa = data.get("gpa", "0.00") # Get the GPA's data, safely return 0.00 when not have GPA's data
                    print(f"{course_id:<12}{mark:<8}{grade:<8}{gpa:<6}") # :<12 mean left-justified width of 12 characters and .1f mean one decimal place

                # Show CGPA
                CGPA = student.calculate_cgpa()
                print("-" * 50)
                print(f"CGPA: {CGPA:.2f}") # :.2f mean 2 decimal places
                print("-" * 50)

        # The student id inputed not exist in the list of student id    
        if found == False:
            print(f"Error: Student ID ({check_student_id}) not found. Please try again.")
            continue # Skip rest of the code and start back from the while True loop

        # Ask if user wants to check another student
        retry = input("\nDisplay student performance again? (Y/N): ")
        if retry == "Y":
            continue # Exit while True loop of choice and go back to while True loop of check_student_id
        else:
            break


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
