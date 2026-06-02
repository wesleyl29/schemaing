import random

from course import Course
from room import Room
from teacher import Teacher
from collections import Counter

class Class:
    CLASSES_AMOUNT = [random.randint(167, 200) for _ in range(10)]

    def __init__(self, period: int, room_id: int, teacher_id: int, course_id: int, class_id: int):
        self.period = period
        self.room_id = room_id
        self.teacher_id = teacher_id
        self.course_id = course_id
        self.class_id = class_id

    def __str__(self):
        return f"INSERT INTO Class ( Period, RoomID, TeacherID, CourseID) VALUES ( {self.period}, {self.room_id}, {self.teacher_id}, {self.course_id} );"

    @property
    def get_id(self):
        return self.class_id

    @staticmethod
    def get_class_list():
        class_list = []
        count = 0
        for period, amount in enumerate(Class.CLASSES_AMOUNT):
            period += 1
            count += 1
            teacher_list = Teacher.get_teacher_list()
            room_list = Room.get_room_list()
            selected_teachers = get_random(teacher_list, amount)
            selected_rooms = get_random(room_list, amount)
            selected_courses = get_random_course(amount)
            for i in range(amount):
                class_list.append(Class(period, selected_rooms[i].get_id, selected_teachers[i].get_teach_id, selected_courses[i].get_course_id, count))
        return class_list




def get_random(directory: list, amount: int) -> list:
    return random.sample(directory, amount)


def get_random_course(amount: int) -> list:
    course_list = Course.get_course_list()
    selected_courses = []
    count = Counter(selected_courses)
    while len(selected_courses) < amount:
        possible_course = random.choice(course_list)
        if count[possible_course] < 5:
            selected_courses.append(possible_course)
    return selected_courses