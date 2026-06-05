import random

from student import Student
from classes import Class

class Roster:
    def __init__(self, class_id, student_id, roster_id):
        self.class_id = class_id
        self.student_id = student_id
        self.roster_id = roster_id

    def __str__(self):
        return f"({self.class_id}, {self.student_id})"
    
    @property
    def get_class_id(self):
        return self.class_id
    
    @property
    def get_student_id(self):
        return self.student_id

    @staticmethod
    def get_roster_list() -> list:
        roster_list = []
        student_list = Student.get_student_list()
        class_list = Class.get_class_list()
        roster_id = 1
        class_id = 0
        for i in range(10):
            amount_list = get_class_list(i)
            random.shuffle(student_list)
            student_id = 1
            for class_index, student_amount in enumerate(amount_list):
                class_id += 1
                for student_index in range(student_amount):
                    roster_list.append(Roster(class_id, student_list[student_index].get_id, roster_id))
                    student_id += 1
                    roster_id += 1

        return roster_list
    
def get_random(directory: list, amount: int) -> list:
    return random.sample(directory, amount)

def get_class_list(period: int) -> list:
    class_amount = Class.CLASSES_AMOUNT[period]
    classes = [25] * class_amount
    remaining_students = 5000 - 25 * class_amount

    while remaining_students > 0:
        for index, students in enumerate(classes):
            classes[index] = students + 1
            remaining_students -= 1
            if remaining_students == 0:
                break

    return classes
