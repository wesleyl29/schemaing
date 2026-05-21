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
            for stud_key, line in enumerate(file):
                student = Student(line.strip(), stud_key+1)
                student_list.append(student)
        return student_list
    
    @property
    def get_id(self):
        return self.student_id
