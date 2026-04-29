import csv

from utility import Utility


class CourseTypes:
    def __init__(self, course_type: str):
        self.course_type = course_type

    def __str__(self):
        return f"INSERT INTO CourseType ( CourseTypeName ) VALUES ( '{self.course_type}' );"

    @staticmethod
    def build_data(file_path: str, column: int) -> list:
        data = set()
        data_as_class = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                validated_string = Utility.validate_string(row[column])

                if not validated_string in data:
                    data_as_class.append(CourseTypes(validated_string))
                    data.add(validated_string)

        return data_as_class


    @staticmethod
    def give_dictionary() -> dict:
        names = CourseTypes.build_data("./CourseName,Type,Department.csv", 1)
        count = 1
        dictionary = {}

        for name in names:
            dictionary[name.course_type] = count
            count += 1

        return dictionary


course_types = CourseTypes.build_data("./CourseName,Type,Department.csv", 1)

with open("./cmd.sql", 'a') as file:
    for course in course_types:
        print(course, file=file)
