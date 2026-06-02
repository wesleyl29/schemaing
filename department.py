from utility import Utility

class Department:
    department_id = 1

    def __init__(self, department_name: str, dept_id: int):
        self.dept_id = dept_id
        self.department_name = department_name

    def __str__(self):
        return f"('{self.department_name}')"

    @staticmethod
    def get_department_list() -> list:
        dept_name_list = Utility.build_data_csv_no_duplicates('/workspaces/schemaing/teacher_file.txt', 1)
        dept_list = []
        for dept_key, name in enumerate(dept_name_list):
            dept_list.append(Department(name[1:], dept_key + 1))
        return dept_list

    @staticmethod
    def get_dept_id(dept: str) -> int:
        list = Department.get_department_list()
        for department in list:
            if department.get_name() == dept:
                return list.index(department)
        return 0

    def get_name(self) -> str:
        return self.department_name