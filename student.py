from utility import Utility

class Student:
    student_dict = {}

    def __init__(self, name: str, student_id: int):
        self.student_id = student_id
        self.name = name
        Student.student_dict[name] = student_id

    def __str__(self):
        return f"INSERT INTO Student VALUES ('{self.name}');"

    @staticmethod
    def get_student_list() -> list:
        list = []
        with open("student_names.txt", 'r') as file:
            for stud_key, line in enumerate(file):
                student = Student(line.strip(), stud_key + 1)
                list.append(student)
        return list
    
    @staticmethod
    def get_id(name: str) -> int:
        return Student.student_dict[name]
    
    @property
    def get_name(self) -> str:
        return self.name
