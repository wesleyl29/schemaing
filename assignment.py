import random

from student import Student
from assignment_types import AssignmentType

# TODO: cannot be done right now
class Assignment:
    def __init__(self, assignment_name: str, assignment_id: int, class_id: int, grade: int, student_id: int):
        self.assignment_name = assignment_name
        self.assignment_id = assignment_id
        self.class_id = class_id
        self.grade = grade
        self.student_id = student_id

    def __str__(self):
        return f"""INSERT INTO Assignment (AssignmentType, AssignmentTypeID, CourseID, Grade, StudentID) VALUES( 
        '{self.assignment_name}', {self.assignment_id}, {self.class_id}, {self.grade}, {self.student_id} );"""

    @staticmethod
    def get_dict() -> dict:
        pass

# TODO: add class dictionary
assignment_count = 0
assignment_id = 1
student_dict = Student.get_dict()
assignment_type_dict = AssignmentType.get_dict()
student = list(student_dict)
assignment_type = list(assignment_type_dict)

with open('./cmd.sql', 'a') as file:
    for i in range(1, 13):
        pass