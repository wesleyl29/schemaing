from student import Student
from department import Department
from teacher import Teacher
from course_types import CourseTypes
from course import Course
from room import Room
from classes import Class
from roster import Roster
from assignment_type import AssignmentType
from assignment_name import AssignmentName
from assignment import Assignment

student_list = Student.get_student_list()
department_list = Department.get_department_list()
teacher_list = Teacher.get_teacher_list()
course_type_list = CourseTypes.get_course_type_list()
course_list = Course.get_course_list()
room_list = Room.get_room_list()
class_list = Class.get_class_list()
roster_list = Roster.get_roster_list()
assignment_type_list = AssignmentType.get_assignment_type_list()
assignment_name_list = AssignmentName.get_assignment_name_list()
assignment_list = Assignment.get_assignment_list()

insert_list = ["INSERT INTO Student (StudentName) VALUES ", 
               "INSERT INTO Department (DepartmentName) VALUES ", 
               "INSERT INTO Teacher (TeacherName, DepartmentID) VALUES ", 
               "INSERT INTO CourseType (CourseTypeName) VALUES",
               "INSERT INTO Course (CourseName, CourseTypeID) VALUES ",
               "INSERT INTO Room (Room) VALUES ",
               "INSERT INTO Class (Period, RoomID, TeacherID, CourseID) VALUES ",
               "INSERT INTO Roster (ClassID, StudentID) VALUES ",
               "INSERT INTO AssignmentType (AssignmentTypeName) VALUES ",
               "INSERT INTO AssignmentNames (AssignmentName, AssignmentTypeID) VALUES ",
               "INSERT INTO Assignment (AssignmentNamesID, StudentID, ClassID, Grade) VALUES "]
every_list = [student_list, department_list, teacher_list, 
            course_type_list, course_list, room_list, 
            class_list, roster_list, assignment_type_list, 
            assignment_name_list, assignment_list]

with open ("cmd.sql", 'a') as f:
    for index, item_list in enumerate(every_list):
        print(insert_list[index], file = f)
        for idx, item in enumerate(item_list):
            stri = ';' if idx == len(item_list) - 1 else ','
            random_list = [str(item), stri]
            print(" ".join(random_list), file = f)


