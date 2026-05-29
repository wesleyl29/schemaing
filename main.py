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
