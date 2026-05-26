from course_types import CourseTypes
from utility import Utility


class Course:
    def __init__(self, course_type_id: int, course: str, course_id: int):
        self.course_type_id = course_type_id
        self.course = course
        self.course_id = course_id

    def __str__(self):
        return f"INSERT INTO Course ( CourseName, CourseTypeID ) VALUES ( '{self.course}', {self.course_type_id} );"

    @staticmethod
    def get_course_dict() -> dict:
        courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
        dictionary = {}
        count = 1

        for course in courses:
            dictionary[course] = count
            count += 1

        return dictionary

@staticmethod
def course_type():
    course_types_dict = CourseTypes.get_dict()
    courses = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
    course_types = list(course_types_dict)
    course_with_type = list(zip(courses, course_types))