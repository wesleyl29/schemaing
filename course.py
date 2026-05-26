from course_types import CourseTypes
from utility import Utility


class Course:
    course_dict = {}

    def __init__(self, course_type_id: int, course_name: str, course_id: int):
        self.course_type_id = course_type_id
        self.course_name =  course_name
        self.course_id = course_id
        Course.course_dict[course_name] = course_id

    def __str__(self):
        return f"INSERT INTO Course ( CourseName, CourseTypeID ) VALUES ( '{self.course_name}', {self.course_type_id} );"

    @property
    def get_course_id(self):
        return self.course_id

    @staticmethod
    def get_id(name: str) -> int:
        return Course.course_dict[name]

    @staticmethod
    def get_course_list() -> list:
        course_names = Utility.build_data_csv("./CourseName,Type,Department.csv", 0)
        course_types = Utility.build_data_csv("./CourseName,Type,Department.csv", 1)
        course_name_type = list(zip(course_names, course_types))
        course_list = []

        for course_id, name_type in enumerate(course_name_type):
            course_name = name_type[0]
            course_type = name_type[1]
            course_type_id = CourseTypes.get_id(course_type)

            course_list.append(Course(course_type_id, course_name, course_id))

        return course_list