from utility import Utility

class Student:
    def __init__(self, name: str):
        self.name = name
        # id auto increments

    def __str__(self):
        return f"INSERT INTO Student VALUES ('{self.name}');"

    @staticmethod
    def get_dict() -> dict:
        stud_dict = {}
        id = 1
        with open("student_names.txt") as file:
            for line in file:
                stud_dict[id] = line.strip()
                id += 1
        return stud_dict


student_list = []
student_dict = Student.get_dict()
student_id = 1
with open("student_names.txt", 'r') as file:
    for line in file:
        student = Student(Utility.validate_string(line.strip()))
        student_list.append(student)

with open("cmd.sql", 'a') as f:
    for student in student_list:
        print(student, file=f)