from course_types import CourseTypes
from utility import Utility


class Course:
    def __init__(self, course_type_id: int, course: str):
        self.course_type_id = course_type_id
        self.course = course

    def __str__(self):
        return f"INSERT INTO Course ( CourseName, CourseTypeID ) VALUES ( '{self.course}', {self.course_type_id} );"

    @staticmethod
    def get_dict() -> dict:
        courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
        dictionary = {}
        count = 1

        for course in courses:
            dictionary[course] = count
            count += 1

        return dictionary


course_types_dict = CourseTypes.get_dict()
courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
course_types = list(course_types_dict)
course_with_type = list(zip(courses, course_types))

with open("./cmd.sql", 'a') as file:
    for values in course_with_type:
        # index 0 is CourseName, index 1 is CourseTypeName
        course_type_id = course_types_dict[values[1]]
        course_name = values[0]

        print(Course(course_type_id, course_name), file=file)