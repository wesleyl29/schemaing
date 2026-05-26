class AssignmentType:
    def __init__(self, assignment_type: str, assignment_id: int):
        self.assignment_type = assignment_type
        self.assignment_id = assignment_id

    @staticmethod
    def get_assignment_type_list():
        minor = AssignmentType("Minor Assessment", 1)
        major = AssignmentType("Major Assessment", 2)
        return [minor, major]

    @staticmethod
    def get_assignment_type_id(type: str):
        for assignment_type in AssignmentType.get_assignment_type_list():
            if assignment_type.get_type == type:
                return assignment_type.get_id
        return 0

    @property 
    def get_type(self):
        return self.assignment_type
    
    @property
    def get_id(self):
        return self.assignment_id
