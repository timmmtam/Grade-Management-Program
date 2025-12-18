def grade_calculation(mark):
    # Function for grade calculation from mark
    if mark >= 80:
        return "A+", "4.00"
    elif mark >= 75:
        return "A", "3.75"
    elif mark >= 70:
        return "A-", "3.50"
    elif mark >= 65:
        return "B+", "3.25"
    elif mark >= 60:
        return "B", "3.00"
    elif mark >= 55:
        return "B-", "2.75"
    elif mark >= 50:
        return "C", "2.50"
    elif mark >= 45:
        return "C-", "2.25"
    elif mark >= 40:
        return "D", "2.00"
    else:
        return "F", "1.50"
