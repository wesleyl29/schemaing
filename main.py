from department import Department
from student import Student
from teacher import Teacher
from assignment_type import AssignmentType

students = Student.get_student_list()
teachers = Teacher.get_teacher_list()
departments = Department.get_department_list()
ass_types = AssignmentType.get_assignment_type_list()
print(AssignmentType.get_assignment_type_id("Minor Assessment"))