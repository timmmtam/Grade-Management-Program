# Module for managing courses

def manage_courses():
    go_back = False

    while (go_back is not True):
        print("\n--------------------------------------")
        print("           Managing Courses           ")
        print("--------------------------------------")
        print("""[1] Add a course
[2] Remove a course
[3] Display course performance summary
[4] Export course performance summary
[5] Go back""")

        # Input from user
        option = input("\nPlease select [1-5]: ")

        match option:
            case "1":
                add_course()
            case "2":
                remove_student()
            case "3":
                display_course_performance()
            case "4":
                export_course_performance()
            case "5":
                go_back = True
            case _:
                print("\nError. Input is not a number 1-5. Please try again.")
                input("Press ENTER to continue...")
