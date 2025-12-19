class Student:
    def __init__(self, student_id, name, email):
        """
        Uses a dictionary to store courses.
        Dictionary structure for enrolled_courses:
        Key: course_id (string)
        Value: {mark: float, grade: string} (another dictionary)
        Example: {"CSC1024": {mark: 92.2, grade: A}}
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = {}

    def calculate_cgpa(self):
        if len(self.enrolled_courses) == 0:
            return 0.00

        total_GPA = 0
        count = 0

        # Loop through each course dictionary
        for course_id, data in self.enrolled_courses.items():
            gpa = data.get("gpa", "0.00")
            total_GPA += float(gpa)
            count += 1

        return round(total_GPA / count, 2)

    def __str__(self):
        return f"{self.name} ({self.student_id})"


class Course:
    """
    Uses a list to store students.
    To add a student, append their student_id to the enrolled_students.
    """
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.enrolled_students = []

    def __str__(self):
        return f"{self.name} ({self.course_id})"
