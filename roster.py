import random

from student import Student
from classes import Class

class Roster:
    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id

    def __str__(self):
        return f"INSERT INTO Roster (ClassID, StudentID) VALUES ({self.class_id}, {self.student_id});"
    

student_dict = Student.get_dict()
class_dict = Class.get_dict()
student_list = list(student_dict.values())

for class_amount in Class.CLASSES_AMOUNT:
    assigned_students = 0
    
    for i in range(class_amount):
        pass