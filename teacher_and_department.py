class Department:
   def __init__(self,department,name):
       self.department = department
       self.name = name

   def __str__(self):
       return "INSERT INTO Department VALUES("+str(self.department)+", \""+self.name+"\");"

   def get_name(self):
       return self.name

   @staticmethod
   def get_dict() -> dict:
       department_dict = {}
       department_id = 1
       with open("teacher_data.txt") as file:
           for line in file:
               if line.strip() == 'break':
                   department_dict[department_id] = file.readline().strip()
                   department_id+=1
       return department_dict

class Teacher:
   def __init__(self,name,teacher,department):
       self.teacher = teacher
       self.name = name
       self.department = department

   def __str__(self):
       return "INSERT INTO Teachers VALUES(\""+self.name+"\", null, \""+self.department+"\");"

   def get_name(self):
       return self.name

   @staticmethod
   def get_dict() -> dict:
       teacher_dict = {}
       teacher_id = 1
       with open('teacher_data.txt') as file:
           for line in file:
                if line.strip() == 'break':
                    file.readline()
                else:
                    teacher_dict[teacher_id] = line.strip()
                    teacher_id+=1
       return teacher_dict

teacher_list = []
department_list = []
dept_dict = Department.get_dict()
teacher_dict = Teacher.get_dict()
dept_id=1
teacher_id=1

department=Department('null','null')
with open('teacher_data.txt') as file:
    for line in file:
        if line.strip()=="break":
            department=Department(dept_id,file.readline().strip())
            department_list.append(department)
            dept_id+=1
        teacher = Teacher(line.strip(),"null",department.get_name())
        if teacher.get_name()=="break":
            pass
        else:
            teacher_list.append(teacher)
            teacher_id+=1

with open('cmd.sql', 'a') as file:
    for teacher in teacher_list:
       print(teacher.__str__(), file = file)
with open('cmd.sql', 'a') as file:
    for department in department_list:
        print(department.__str__(), file=file)