import csv

course_type = []

def get_data():
    file_path = "CourseName,Type,Department.csv"

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            course_type.append(f"( {row[1]} ), \n")

def __str__():
    statement = "INSERT INTO CourseType(CourseTypeName) VALUES \n"

    for course in course_type:
        if course != course_type[-1]:
            statement += course
        else:
            statement += course.replace(",", "")

    return statement

get_data()
course_type = list(dict.fromkeys(course_type))
print(__str__())