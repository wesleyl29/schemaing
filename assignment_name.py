class AssignmentName:
    def __init__(self, assignment_name: str, assignment_name_id: int, assignment_type_id: int):
        self.assignment_name = assignment_name
        self.assignment_name_id = assignment_name_id
        self.assignment_type_id = assignment_type_id
    def __str__(self):
        return f"('{self.assignment_name}')"
    
    @staticmethod
    def get_assignment_name_list() -> list:
        assignment_name_list = []
        assignment_id = 1

        for i in range(1, 4):
            assignment_name_list.append(AssignmentName(f"Major Assessment {i}", assignment_id, 2))
            assignment_id += 1

        for i in range(1, 16):
            assignment_name_list.append(AssignmentName(f"Minor Assessment {i}", assignment_id, 1))

        return assignment_name_list