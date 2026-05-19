class Department:
    def __init__(self, department_name: str):
        self.department_name = department_name

    def __str__(self):
        return f"INSERT INTO Department (DepartmentName) VALUES ('{self.department_name}');"

    @staticmethod
    def get_dict() -> dict:
        dept_dict = {}
        dept_id = 1
        with open("teacher_file.txt", 'r') as file:
            for line in file:
                if line.strip().split(', ', 1)[1] in dept_dict:
                    pass
                else:
                    dept_dict[line.strip().split(', ',1)[1]] = dept_id
                    dept_id += 1
        return dept_dict

department_dict = Department.get_dict()
department_list = []
for key in department_dict:
    dept = Department(key)
    department_list.append(dept)

with open("cmd.sql",'a') as f:
    for dept in department_list:
        print(dept, file = f)