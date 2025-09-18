#!/usr/bin/env python3

from Student_Objects import Student

def main():
    print("The Student Viewer Program")
    print()

    # Create a tuple of Students, or an immutable (unchangeable) list
    students = (Student("Ty", "Monsale", "Junior", "IIT"),
                Student("Jalen", "Gibson", "Junior", "IIT"),
                Student("Alex", "Reynolds", "Junior", "IIT"),)
    
    for student in students:
        student.getClassCredits()
        student.getClassSchedule()

if __name__ == "__main__":
    main()