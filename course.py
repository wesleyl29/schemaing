from course_types import CourseTypes
from utility import Utility


class Course:
    def __init__(self, foreign_id: int, course: str):
        self.foreign_id = foreign_id
        self.course = course

    def __str__(self):
        return f"INSERT INTO Course ( CourseName, CourseTypeID ) VALUES ( '{self.course}', {self.foreign_id} );"

    @staticmethod
    def get_dictionary() -> dict:
        courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
        dictionary = {}
        count = 1

        for course in courses:
            dictionary[course] = count
            count += 1

        return dictionary


course_types_dict = CourseTypes.get_dictionary()
courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
course_types = Utility.build_data_csv("./CourseName,Type,Department.csv", 1)
course_with_type = list(zip(courses, course_types))

with open("./cmd.sql", 'a') as file:
    for values in course_with_type: # index 0 is CourseName, index 1 is CourseTypeName
        foreign_key = course_types_dict[values[1]]
        course_name = values[0]

        print(Course(foreign_key, course_name), file=file)

print(Course.get_dictionary())