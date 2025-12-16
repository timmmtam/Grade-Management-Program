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
        print(f"Complete! Course {course_name}({course_id}) has been successfully added to the system.")
        retry = input("Do you want to add another course? (Y/N): ")
        if (retry.upper() == "Y"):
            continue
        else:
            return


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
