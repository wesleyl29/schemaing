import random

from roster import Roster
from assignment_name import AssignmentName

class Assignment:
    def __init__(self, assignment_name_id: int, roster_id: int, grade: int):
        self.assignment_name_id = assignment_name_id
        self.roster_id = roster_id
        self.grade = grade

    def __str__(self):
        return f"({self.assignment_name_id}, {self.roster_id}, {self.grade} )"

    @staticmethod
    # TODO: rewrite assignment to use assignment_name for efficency
    def get_assignment_list() -> list:
        assignment_list = []
        roster_list = Roster.get_roster_list()
        assignment_name_list = AssignmentName.get_assignment_name_list()
        for roster in roster_list:
            for i in range(3):
                assignment_list.append(Assignment(assignment_name_list[i].get_id, 
                                                  roster.get_id,
                                                  random.randint(75,100)
                                                  ))
            for i in range(15):
                assignment_list.append(Assignment(assignment_name_list[i + 3].get_id, 
                                                  roster.get_id,
                                                  random.randint(75,100)
                                                  ))
        return assignment_list
    