import random

from assignment_type import AssignmentType
from roster import Roster

class Assignment:
    def __init__(self, assignment_name: str, assignment_id: int, assignment_type_id: int, class_id: int, grade: int, student_id: int):
        self.assignment_name = assignment_name
        self.assignment_id = assignment_id
        self.assignment_type_id = assignment_type_id
        self.class_id = class_id
        self.grade = grade
        self.student_id = student_id

    def __str__(self):
        return f"('{self.assignment_name}', {self.assignment_id}, {self.class_id}, {self.grade}, {self.student_id} )"

    @staticmethod
    def get_assignment_list() -> list:
        assignment_list = []
        assignment_id = 1
        roster_list = Roster.get_roster_list()
        for roster in roster_list:
            for i in range(1, 4):
                assignment_list.append(Assignment("Major Assessment " + str(i), assignment_id, 2, roster.get_class_id, random.randint(75,100), roster.get_student_id))
                assignment_id += 1
            for i in range(1, 13):
                assignment_list.append(Assignment("Minor Assessment " + str(i), assignment_id, 1, roster.get_class_id, random.randint(75,100), roster.get_student_id))
                assignment_id += 1
        return assignment_list
    