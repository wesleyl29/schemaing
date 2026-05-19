from department import Department
from utility import Utility

class Teacher:
    def __init__(self, teacher_name: str, dept_id: int):
        self.teacher_name = teacher_name
        self.dept_id = dept_id

    def __str__(self):
        return f"INSERT INTO Teacher (TeacherName, DepartmentID) VALUES ('{self.teacher_name}', {self.dept_id});"

    @staticmethod
    def get_dict() -> dict:
        teach_dict = {}
        teach_id = 1
        with open("teacher_file.txt") as f:
            for line in f:
                teach_dict[line.strip().split(',',1)[0]] = teach_id
                teach_id += 1
        return teach_dict

teacher_list = []
dept_dict = Department.get_dict()
with open("teacher_file.txt", 'r') as f:
    for line in f:
        dept = line.strip().split(', ',1)[1]
        teacher = Teacher(line.strip().split(',',1)[0], dept_dict[dept])
        teacher_list.append(Utility.validate_string(teacher))

with open("cmd.sql",'a') as f:
    for teach in teacher_list:
        print(teach, file = f)