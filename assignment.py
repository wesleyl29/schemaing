import random

from assignment_type import AssignmentType
from roster import Roster

# TODO: cannot be done right now
class Assignment:
    def __init__(self, assignment_name: str, assignment_id: int, assignment_type_id: int, class_id: int, grade: int, student_id: int):
        self.assignment_name = assignment_name
        self.assignment_id = assignment_id
        self.assignment_type_id = assignment_type_id
        self.class_id = class_id
        self.grade = grade
        self.student_id = student_id

    def __str__(self):
        return f"""INSERT INTO Assignment (AssignmentType, AssignmentTypeID, CourseID, Grade, StudentID) VALUES( 
        '{self.assignment_name}', {self.assignment_id}, {self.class_id}, {self.grade}, {self.student_id} );"""

    @staticmethod
    def get_assignment_list() -> list:
        assignment_list = []
        assignment_id = 1
        major_dict = get_major_class_dict()
        minor_dict = get_minor_class_dict()
        roster_list = Roster.get_roster_list()
        MAJOR_COUNT = 3
        MINOR_COUNT = 12
        for roster in roster_list:
            for i in range(MAJOR_COUNT):
                assignment_list.append(Assignment(major_dict[i], assignment_id, roster.get_class_id, random.randint(75,100), roster.get_student_id))
                assignment_id += 1
            for i in range(MINOR_COUNT):
                assignment_list.append(Assignment(minor_dict[i], assignment_id, roster.get_class_id, random.randint(75,100), roster.get_student_id))
                assignment_id += 1
    