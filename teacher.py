class Teacher:
    def __init__(self, teacher_name: str, dept_id: int):
        self.teacher_name = teacher_name
        self.dept_id = dept_id

    def __str__(self):
        return "INSERT INTO Teacher (TeacherName, DepartmentID) VALUES (\""+self.teacher_name+"\""+str(self.dept_id)+");"

    @staticmethod
    def get_dict() -> dict:
        teach_dict = {}
        teach_id = 1
        with open('teacher_file.txt') as f:
            for line in f:
                teach_dict[line.strip().split(',',1)[0]]=teach_id
                teach_id+=1
        return teach_dict

dicti = Teacher.get_dict()
print(dicti.items())