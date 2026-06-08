import random

from roster import Roster
from assignment_name import AssignmentName

class Assignment:
    def __init__(self, assignment_name_id: int, student_id: int, class_id:int, grade: int):
        self.assignment_name_id = assignment_name_id
        self.student_id = student_id
        self.class_id = class_id
        self.grade = grade

    def __str__(self):
        return f"({self.assignment_name_id}, {self.student_id}, {self.class_id}, {self.grade} )"

    @staticmethod
    def get_assignment_list() -> list:
        assignment_list = []
        roster_list = Roster.get_roster_list()
        assignment_name_list = AssignmentName.get_assignment_name_list()
        for roster in roster_list:
            for i in range(3):
                assignment_list.append(Assignment(assignment_name_list[i].get_id, 
                                                  roster.get_student_id,
                                                  roster.get_class_id,
                                                  random.randint(75,100)
                                                  ))
            for i in range(3, len(assignment_name_list)):
                assignment_list.append(Assignment(assignment_name_list[i].get_id, 
                                                  roster.get_student_id,
                                                  roster.get_class_id,
                                                  random.randint(75,100)
                                                  ))
        return assignment_list
    