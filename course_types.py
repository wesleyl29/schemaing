import csv

from utility import Utility


class CourseTypes:
    def __init__(self, course_type: str):
        self.course_type = course_type

    def __str__(self):
        return f"INSERT INTO CourseType ( CourseTypeName ) VALUES ( '{self.course_type}' );"

    @staticmethod
    def get_dictionary() -> dict:
        courses = Utility.build_data_csv_no_duplicates("./CourseName,Type,Department.csv", 1)
        count = 1
        dictionary = {}

        for course in courses:
            dictionary[CourseTypes(course).course_type] = count
            count += 1

        return dictionary


course_types = Utility.build_data_csv_no_duplicates("./CourseName,Type,Department.csv", 1)

with open("./cmd.sql", 'a') as file:
    for course in course_types:
        print(CourseTypes(course), file=file)