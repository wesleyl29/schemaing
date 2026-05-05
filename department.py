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
