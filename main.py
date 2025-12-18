# Library and Module Imports
from package import students as s
from package import courses as c
from package.classes import Student, Course
from package.config import student_list, course_list


def load_data():
    # Load data from the three text files
    print("===DATA INITIALIZATION===")
    try:
        print("Retrieving data from students.txt...")
        with open("students.txt", "r") as f:
            for line in f:
                section = line.strip().split(",")
                student_list.append(Student(section[0], section[1],
                                            section[2]))
        print(f"{len(student_list)} student(s) found.")
    except FileNotFoundError:
        print("students.txt not found. Creating students.txt...")
        with open("students.txt", "a") as f:
            pass

    try:
        print("Retrieving data from courses.txt...")
        with open("courses.txt", "r") as f:
            for line in f:
                section = line.strip().split(",")
                course_list.append(Course(section[0], section[1]))
        print(f"{len(course_list)} course(s) found.")
    except FileNotFoundError:
        print("courses.txt not found. Creating courses.txt...")
        with open("courses.txt", "a") as f:
            pass

    try:
        print("Assigning data from grades.txt...")
        with open("grades.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                section = line.strip().split(",")
                for student in student_list:
                    if (student.student_id == section[0]):
                        for course in course_list:
                            if (course.course_id == section[1]):
                                try:
                                    student.enrolled_courses[course.course_id] = {
                                            "mark": section[2],
                                            "grade": section[3],
                                            "gpa": section[4]}
                                except IndexError:
                                    student.enrolled_courses[course.course_id] = {}
    except FileNotFoundError:
        print("grades.txt not found. Creating grades.txt...")
        with open("grades.txt", "a") as f:
            pass
    print("Done!")


def display_main_menu():
    exit_program = False

    while (exit_program is not True):
        print("\n--------------------------------------")
        print("        Student Grading System        ")
        print("--------------------------------------")
        print("[1] Manage Students\n[2] Manage Courses\n[3] Exit")

        # User Input
        option = input("\nPlease select [1-3]: ")

        match option:
            case "1":
                s.manage_students()
            case "2":
                c.manage_courses()
            case "3":
                exit_program = True
                print("\nExiting program...")
            case _:
                print("\nError. Input is not a number 1-3. Please try again.")
                input("Press ENTER to continue...")


if (__name__ == "__main__"):
    load_data()
    display_main_menu()
