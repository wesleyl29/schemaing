import csv

from course_types import CourseTypes


class Course(CourseTypes):
    def __init__(self, foreign_id: int, name: str, course_type: str):
        super().__init__(course_type)
        self.foreign_id = foreign_id
        self.name = name

    def __str__(self):
        return f"INSERT INTO Course ( CourseName, CourseTypeID ) VALUES ( '{self.name}', {self.foreign_id} );"

    @staticmethod
    def get_dictionary() -> dict: # from parent
        return CourseTypes.give_dictionary()

    @staticmethod
    def give_dictionary() -> dict:




