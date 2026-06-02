from department import Department
from utility import Utility

class Teacher:
    def __init__(self, teacher_name: str, teacher_id: int, dept_id: int):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.dept_id = dept_id

    def __str__(self):
        return f"INSERT INTO Teacher (TeacherName, DepartmentID) VALUES ('{self.teacher_name}', {self.dept_id});"

    @staticmethod
    def get_teacher_list() -> list:
        teacher_list = []
        with open("teacher_file.txt", 'r') as f:
            for id, line in enumerate(f):
                dept = line.strip().split(', ',1)[1]
                teacher = Teacher(Utility.validate_string(line.strip().split(',',1)[0]), id+1, Department.get_dept_id(dept)+1)
                teacher_list.append(teacher)
        return teacher_list
    
    @property
    def get_teach_id(self):
        return self.teacher_id
    