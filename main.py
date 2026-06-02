from student import Student
from department import Department
from teacher import Teacher
from course_types import CourseTypes
from course import Course
from room import Room
from classes import Class
from roster import Roster
from assignment_type import AssignmentType
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
assignment_list = Assignment.get_assignment_list()

every_list = [student_list, department_list, teacher_list, course_type_list, course_list, room_list, class_list, roster_list, assignment_type_list, assignment_list]
with open ("cmd.sql", 'a') as f:
    for item_list in every_list:
        for item in item_list:
            print(item, file = f)