class Student:
    def __init__(self,name):
        self.name=name
        #id auto increments

    def __str__(self):
        return "INSERT INTO Student VALUES (null, \""+self.name+"\");"

    def get_name(self):
        return self.name

student_list = []
student_dict = {}
student_id = 1
with open('student_names.txt') as file:
    for line in file:
        student = Student(line.strip())
        student_list.append(student)
        student_dict[student_id] = student.get_name()
        student_id+=1

print(student_dict.items())
for student in student_list:
    with open('cmd.sql','a') as f:
        print(student.__str__(), file = f)