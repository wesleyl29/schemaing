from utility import Utility

class Student:
    

    def __init__(self, name: str, student_id: int):
        self.student_id = student_id
        self.name = name
        # id auto increments

    def __str__(self):
        return f"INSERT INTO Student VALUES ('{self.name}');"

    @staticmethod
    def student_cmd() -> list:
        student_list = []
        with open("student_names.txt", 'r') as file:
            for line in file:
                student = Student(line.strip())
                student_list.append(Utility.validate_string(line.strip()))
