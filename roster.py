import random

from student import Student
from classes import Class

class Roster:
    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id

    def __str__(self):
        return f"INSERT INTO Roster (ClassID, StudentID) VALUES ({self.class_id}, {self.student_id});"
    
def get_class_list(period: int) -> list:
    class_amount = Class.CLASSES_AMOUNT[period]
    classes = [25] * class_amount
    remaining_students = 5000 - 25 * class_amount

    while remaining_students > 0:
        for index, students in enumerate(classes):
            classes[index] = students + 1
            remaining_students -= 1

    return classes


student_dict = Student.get_dict()
class_dict = Class.get_dict()

for i in range(10):
    classes = get_class_list