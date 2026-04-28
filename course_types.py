import csv


class CourseTypes:
    def __init__(self, course_type):
        self.course_type = course_type

    def __str__(self):
        return "INSERT INTO CourseType ( CourseTypeName ) VALUES ( '" + self.course_type + "' )"


def validate_string(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Argument must be a string.")

    return string.replace("'", "''")

course_types = set()
course_types_class = []
file_path = "./CourseName,Type,Department.csv"

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        validated_string = validate_string(row[1])
        
        if not validated_string in course_types:
            course_types_class.append(CourseTypes(validated_string))
            course_types.add(validated_string)

with open("./cmd.sql", 'a') as file:
    for course in course_types_class:
        print(course, file = file)