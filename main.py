from department import Department
from student import Student
from teacher import Teacher

students = Student.get_student_list()
hi = students[4999].get_name
print(Student.get_id(hi))