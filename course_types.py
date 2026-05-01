import csv

from utility import Utility


class CourseTypes:
    def __init__(self, course_type: str):
        self.course_type = course_type

    def __str__(self):
        return f"INSERT INTO CourseType ( CourseTypeName ) VALUES ( '{self.course_type}' );"

    @staticmethod
    def get_dictionary() -> dict:
        courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 1, CourseTypes)
        count = 1
        dictionary = {}

        for course in courses:
            dictionary[course.course_type] = count
            count += 1

        return dictionary


course_types = Utility.build_data_csv("./CourseName,Type,Department.csv", 1, CourseTypes)

with open("./cmd.sql", 'a') as file:
    for course in course_types:
        print(course, file=file)
