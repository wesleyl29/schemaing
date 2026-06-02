from utility import Utility


class CourseTypes:
    course_type_dict = {}

    def __init__(self, course_type: str, course_type_id: int):
        self.course_type = course_type
        self.course_type_id = course_type_id
        CourseTypes.course_type_dict[course_type] = course_type_id

    def __str__(self):
        return f"INSERT INTO CourseType ( CourseTypeName ) VALUES ( '{self.course_type}' );"

    @staticmethod
    def get_id(name: str) -> int:
        return CourseTypes.course_type_dict[name]+1

    @staticmethod
    def get_course_type_list() -> list:
        course_types_name = Utility.build_data_csv_no_duplicates("./CourseName,Type,Department.csv", 1)
        course_types = []

        for course_type_id, course_type_name in enumerate(course_types_name):
            course_types.append(CourseTypes(course_type_name, course_type_id))

        return course_types