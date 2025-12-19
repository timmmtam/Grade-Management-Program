# Module for managing courses
from .config import student_list, course_list
from .classes import Course
from .utils import courses_available, students_available


def display_course():
    # Display the list of courses
    print("\n--------------------------------------")
    print("             Courses List             ")
    print("--------------------------------------")
    for course in course_list:
        print(course)
    input("\nPress ENTER to return...")


def add_course():
    print("\n--------------------------------------")
    print("             Add a Course             ")
    print("--------------------------------------")
    while True:
        course_id = input("Enter a new Course ID: ")
        course_id = course_id.upper()
        if (len(course_id) > 8 or not course_id):
            print("\nError. Course ID must be 1-8 characters long.")
            input("\nPress ENTER to return...")
            return
        for course in course_list:
            if (course_id == course.course_id):
                print("\nError. Course already exists.")
                input("\nPress ENTER to return...")
                return
        while True:
            course_name = input("Enter the course's name: ")
            if (all(char.isalpha() or char.isspace() for char in course_name)):
                break
            else:
                print("Error. Course name must be contain alphabets only.")
                retry = input("Try again? (Y/N): ")
                if (retry.upper() == "Y"):
                    continue
                else:
                    return
        new_course = Course(course_id, course_name)
        course_list.append(new_course)
        with open("courses.txt", "a") as f:
            f.write(f"{course_id},{course_name}\n")
        print(f"Success! {course_name}({course_id}) has been added.")
        retry = input("Do you want to add another course? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            return


def display_course_performance():
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

    print("\n--------------------------------------")
    print("      Display Course Performance      ")
    print("--------------------------------------")
    print("\nCourse list\n---------------------")
    for course in course_list:
        print(course)
    course_id = input("\nEnter Course ID to display summary for: ")
    course_id = course_id.upper()

    students_in_course = []
    marks = []

    for student in student_list:
        if course_id in student.enrolled_courses:
            students_in_course.append(student)
            try:
                marks.append(float(student.enrolled_courses[course_id]["mark"]))
            except KeyError:
                print(f"\nError. Data for {student.name} is not complete.")
                input("\nPress ENTER to return...")
                return

    if len(marks) == 0:
        print(f"\nNo students found enrolled in {course_id}.")
        input("\nPress ENTER to return...")
        return

    average_mark = sum(marks) / len(marks)
    lowest_mark = min(marks)
    highest_mark = max(marks)

    print(f"\nStudents in {course_id}:")
    print("---------------------------------")
    for student in students_in_course:
        info = student.enrolled_courses[course_id]
        print(f"{student.name} ({student.student_id}) - Mark: {info['mark']}")

    print(f"\nPerformance summary for {course_id}:")
    print("---------------------------------")
    print(f"Average mark: {average_mark:.2f}")
    print(f"Lowest mark:  {lowest_mark}")
    print(f"Highest mark: {highest_mark}")

    input("\nPress ENTER to return...")


def export_course_performance():
    if (students_available(student_list) is False):
        print("\nError: No data of students available!")
        input("\nPress ENTER to return...")
        return

    if (courses_available(course_list) is False):
        print("\nError: No data of courses available!")
        input("\nPress ENTER to return...")
        return

    print("\n--------------------------------------")
    print("       Export Course Performance      ")
    print("--------------------------------------")
    print("\nCourse list\n---------------------")
    for course in course_list:
        print(course)

    course_id = input("\nEnter Course ID to export: ")
    course_id = course_id.upper()
    if (course_id not in (course.course_id for course in course_list)):
        print("\nError. Course does not exist.")
        input("\nPress ENTER to return...")
        return

    students_in_course = []
    marks = []

    for student in student_list:
        if course_id in student.enrolled_courses:
            students_in_course.append(student)
            try:
                marks.append(float(student.enrolled_courses[course_id]["mark"]))
            except KeyError:
                print(f"\nError. Data for {student.name} not complete.")
                input("\nPress ENTER to return...")
                return

    if len(marks) == 0:
        print(f"\nNo students found enrolled in {course_id}.")
        input("\nPress ENTER to return...")
        return

    average_mark = sum(marks) / len(marks)
    lowest_mark = min(marks)
    highest_mark = max(marks)

    report_title = f"{course_id} Course Performance Summary"

    report_filename = f"{report_title.replace(' ', '_')}.txt"

    with open(report_filename, "w") as report:
        report.write(f"{report_title}\n\n")

        with open("grades.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if (len(data) > 3):
                    if data[1] == course_id:
                        report.write(f"Student ID: {data[0]} Marks: {data[2]}")
                        report.write(f", Grade: {data[3]}\n")
                else:
                    print("\nError. Data is incomplete")
                    input("\nPress ENTER to return...")
                    return
            report.write("\nCourse Performance Summary\n")
            report.write("-----------------------------\n")
            report.write(f"Lowest Mark: {lowest_mark}\n")
            report.write(f"Highest Mark: {highest_mark}\n")
            report.write(f"Marks Average: {average_mark}")

    print(f"Course report saved as {report_filename}")
    input("\nPress ENTER to continue...")


def manage_courses():
    go_back = False

    while (go_back is not True):
        print("\n--------------------------------------")
        print("           Managing Courses           ")
        print("--------------------------------------")
        print("""[1] Display courses
[2] Add a course
[3] Display course performance summary
[4] Export course performance summary
[5] Go back""")

        # Input from user
        option = input("\nPlease select [1-5]: ")

        match option:
            case "1":
                display_course()
            case "2":
                add_course()
            case "3":
                display_course_performance()
            case "4":
                export_course_performance()
            case "5":
                go_back = True
            case _:
                print("\nError. Input is not a number 1-5. Please try again.")
                input("Press ENTER to continue...")
