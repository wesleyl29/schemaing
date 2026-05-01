class Student:
    def __init__(self,name):
        self.name=name
        #id auto increments

    def __str__(self):
        return "INSERT INTO Student VALUES (null, \""+self.name+"\");"

    def getName(self):
        return self.name

studentList = []
studentDict = {}
studentID = 1
with open('student_names.txt') as file:
    for line in file:
        student = Student(line.strip())
        studentList.append(student)
        studentDict[studentID] = student.getName()
        studentID+=1

print(studentDict.items())
for student in studentList:
    with open('cmd.sql','a') as f:
        print(student.__str__(), file = f)