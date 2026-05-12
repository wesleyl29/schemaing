import random

from course import Course
from room import Room
from teacher import Teacher


class Class:
    # remove seed after testing
    random.seed(42)
    CLASSES_AMOUNT = [random.randint(167, 200) for _ in range(10)]

    def __init__(self, period: int, room_id: int, teacher_id: int, course_id: int):
        self.period = period
        self.room_id = room_id
        self.teacher_id = teacher_id
        self.course_id = course_id

    def __str__(self):
        return f"INSERT INTO Class ( Period, RoomID, TeacherID, CourseID) VALUES ( {self.period}, {self.room_id}, {self.teacher_id}, {self.course_id} );"

    @staticmethod
    def get_dict() -> dict:
        count = 1
        class_dict = {}

        for index, num in enumerate(Class.CLASSES_AMOUNT):
            for i in range(num):
                class_dict[f"c{i}p{index + 1}"] = count
                count += 1

        return class_dict


def get_random(dictionary: dict, amount: int) -> list:
    return random.sample(list(dictionary.values()), amount)


def get_random_duplicates(dictionary: dict, amount: int) -> list:
    return random.choices(list(dictionary.values()), k=amount)


course_dictionary = Course.get_dict()
room_dictionary = Room.get_dict()
teacher_dictionary = Teacher.get_dict()

with open("./cmd.sql", 'a') as file:
    for period, amount_of_classes in enumerate(Class.CLASSES_AMOUNT):
        teachers = get_random(teacher_dictionary, amount_of_classes)
        rooms = get_random(room_dictionary, amount_of_classes)
        courses = get_random_duplicates(course_dictionary, amount_of_classes)
        teachers_rooms_courses = list(zip(teachers, rooms, courses))

        for teacher, room, course in teachers_rooms_courses:
            print(Class(period + 1, teacher, room, course), file=file)