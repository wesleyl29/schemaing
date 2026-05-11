import random

from course import Course
from room import Room
from teacher import Teacher

class Class:
    def __init__(self, period: int, room_id: int, teacher_id: int, course_id: int):
        self.period = period
        self.room_id = room_id
        self.teacher_id = teacher_id
        self.course_id = course_id

    def __str__(self):
        return f"INSERT INTO Class ( Period, RoomID, TeacherID, CourseID, ClassID ) VALUES ( {self.period}, {self.room_id}, {self.teacher_id}, {self.course_id} );"

    @staticmethod
    def get_dict() -> dict:
        count = 1
        class_dict = {}
        object = Class(1,1,1,1)
        amount = object.generate_class()
        for num in amount:
            for i in range(num):
                class_dict[f"c{i}p{amount}"] = count
                count += 1
        return class_dict 
        
course_dictionary = Course.get_dict()
room_dictionary = Room.get_dict()
teacher_dictionary = Teacher.get_dict()

