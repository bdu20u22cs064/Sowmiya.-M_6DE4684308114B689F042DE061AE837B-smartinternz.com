def sort_students(List_of_Students):
    sorted_studentsList = sorted(List_of_Students, key=lambda x: x.cgpa, reverse=True)
    return sorted_studentsList


class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


students = [
    Student("xx", "1", 8.9),
    Student("yy", "2", 9.0),
    Student("zz", "3", 7.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")