from department import Department
from student import Student
from teacher import Teacher

departments = Department.get_department_list()
for dept in departments:
    print(dept)