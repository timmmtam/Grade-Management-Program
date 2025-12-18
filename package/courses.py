# Module for managing courses
from .config import student_list, course_list
from .classes import Course


def add_course():
    print("\n--------------------------------------")
    print("             Add a Course             ")
    print("--------------------------------------")
    while True:
        course_id = input("Enter a new Course ID: ")
        course_id.upper()
        for course in course_list:
            if (course_id == course.course_id):
                print("Error. Course already exists.")
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
    print("\n--------------------------------------")
    print("      Display Course Performance      ")
    print("--------------------------------------")
    course_id = input("\nEnter Course ID to display summary for: ")

    students_in_course = []
    marks = []

    for student in student_list:
        if course_id in student.enrolled_courses:
            students_in_course.append(student)
            marks.append(float(student.enrolled_courses[course_id]["mark"]))

    if len(marks) == 0:
        print(f"\nNo students found enrolled in {course_id}.")
        input("\nPress ENTER to continue...")
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

    input("\nPress ENTER to continue...")


def export_course_performance():
    print("\n--------------------------------------")
    print("       Export Course Performance      ")
    print("--------------------------------------")
    course_id = input("Enter Course ID: ")
    if (course_id not in course_list):
        print("\nError. Course does not exist.")
        input("\nPress ENTER to continue...")
        return

    report_title = input("Enter report title: ").strip()
    if not report_title:
        print("Report title is required.\n")
        return

    report_filename = f"{report_title.replace(' ', '_')}.txt"

    with open(report_filename, "w") as report:
        report.write(f"{report_title}\n\n")
        report.write(f"Course ID: {course_id}\n")

        with open("grades.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == course_id:
                    report.write(f"Student ID: {data[0]} Marks: {data[2]}, Grade: {data[3]}\n")

    print(f"Course report saved as {report_filename}\n")


def manage_courses():
    go_back = False

    while (go_back is not True):
        print("\n--------------------------------------")
        print("           Managing Courses           ")
        print("--------------------------------------")
        print("""[1] Add a course
[2] Display course performance summary
[3] Export course performance summary
[4] Go back""")

        # Input from user
        option = input("\nPlease select [1-5]: ")

        match option:
            case "1":
                add_course()
            case "2":
                display_course_performance()
            case "3":
                export_course_performance()
            case "4":
                go_back = True
            case _:
                print("\nError. Input is not a number 1-4. Please try again.")
                input("Press ENTER to continue...")
