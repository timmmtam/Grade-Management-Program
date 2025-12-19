#  Module for managing students
from .config import student_list, course_list
from .classes import Student
from .utils import grade_calculation, courses_available, students_available


def display_students():
    # Display the list of students with their student_id
    print("\n--------------------------------------")
    print("             Student List             ")
    print("--------------------------------------")
    for student in student_list:
        print(student)
    input("\nPress ENTER to return...")


def add_student():
    print("\n--------------------------------------")
    print("            Add a Student             ")
    print("--------------------------------------")
    while True:
        while True:
            student_id = input("Enter a new Student ID: ")
            if (student_id.isdigit() is False or not student_id):
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
                input("Press ENTER to return...")
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
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

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
            input("\nPress ENTER to return...")
            return

        print("\nCourse list\n---------------------")
        for course in course_list:
            print(course)

        course_id = input("\nSelect the Course ID to enroll the student in: ")
        if (course_id not in (course.course_id for course in course_list)):
            print("\nError. Course does not exist.")
            input("\nPress ENTER to return...")
            return
        for student in student_list:
            if (student_id == student.student_id):
                for key in student.enrolled_courses:
                    if (key == course_id):
                        print("\nError.")
                        print("Student is already enrolled in this course.")
                        input("\nPress ENTER to return...")
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
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

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
            input("\nPress ENTER to return...")
            return

        print(f"\nEnrolled courses for {student_id}")
        print("------------------------------------")
        for student in student_list:
            if (student_id == student.student_id):
                for key in student.enrolled_courses:
                    print(f"{key}")

        enrolled = False
        course_id = input("\nInput Course ID to record marks for: ")
        for student in student_list:
            if (student_id == student.student_id):
                if course_id in student.enrolled_courses:
                    enrolled = True
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
            if ((marks < 0) or (marks > 100)):
                print("\nError. Marks must be in range 0 - 100.")
                input("\nPress ENTER to retry...")
                continue
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
            input("\nPress ENTER to retry...")
            continue
        retry = input("\nRecord marks again? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            break


def display_student_performance():
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

    while True:
        print("\n--------------------------------------")
        print("      Display Student Performance     ")
        print("--------------------------------------")
        print("\nStudent list\n---------------------")
        for student in student_list:
            print(student)
        print()
        student_id = input("\nEnter Student ID to display performance: ")

        found = False
        for student in student_list:
            if student.student_id == student_id:
                found = True
                print(f"\nStudent: {student.name} ({student.student_id})")
                print(f"Email:{student.email}")
                print("-" * 50)

                print(f"{'Course ID':<12} {'Mark':<8}{'Grade':<8}{'GPA':<6}")

                for course_id, data in student.enrolled_courses.items():
                    mark = data.get("mark", "0")
                    grade = data.get("grade", "N/A")
                    gpa = data.get("gpa", "0.00")
                    print(f"{course_id:<12}{mark:<8}{grade:<8}{gpa:<6}")

                CGPA = student.calculate_cgpa()
                print("-" * 50)
                print(f"CGPA: {CGPA:.2f}")
                print("-" * 50)

        if found is False:
            print(f"Error: Student ID ({student_id}) not found.")
            input("Press ENTER to return...")
            return

        retry = input("\nDisplay student performance again? (Y/N): ")
        if retry.upper() == "Y":
            continue
        else:
            break


def export_student_performance():
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

    print("\n--------------------------------------")
    print("      Export Student Performance      ")
    print("--------------------------------------")
    print("\nStudent list\n---------------------")
    for student in student_list:
        print(student)

    student_id = input("\nEnter Student ID to export: ")
    if (student_id not in (student.student_id for student in student_list)):
        print("\nError. Student does not exist.")
        input("\nPress ENTER to return...")
        return

    report_title = f"{student_id} Performance Summary"

    report_filename = f"{report_title.replace(' ', '_')}.txt"

    with open(report_filename, "w") as report:
        report.write(f"{report_title}\n\n")

        found = False
        for student in student_list:
            if student.student_id == student_id:
                found = True
                report.write(f"Student: {student.name} ({student.student_id})\n")
                report.write(f"Email:{student.email}\n")
                report.write("-" * 50 + "\n")

                report.write(f"{'Course ID':<12} {'Mark':<8}{'Grade':<8}{'GPA':<6}\n")

                for course_id, data in student.enrolled_courses.items():
                    mark = data.get("mark", "0")
                    grade = data.get("grade", "N/A")
                    gpa = data.get("gpa", "0.00")
                    report.write(f"{course_id:<12}{mark:<8}{grade:<8}{gpa:<6}\n")

                CGPA = student.calculate_cgpa()
                report.write("-" * 50 + "\n")
                report.write(f"CGPA: {CGPA:.2f}\n")
                report.write("-" * 50 + "\n")

        if found is False:
            print(f"Error: Student ID ({student_id}) not found.")
            input("Press ENTER to return...")
            return

    print(f"Student report saved as {report_filename}")
    input("\nPress ENTER to continue...")


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
                display_students()
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
