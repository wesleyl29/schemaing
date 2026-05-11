import random

from student import Student
from classes import Class

class Roster:
    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id

    def __str__(self):
        return f"INSERT INTO Roster (ClassID, StudentID) VALUES (1, "+self.student_id+");"


