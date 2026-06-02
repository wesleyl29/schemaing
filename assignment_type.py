class AssignmentType:
    def __init__(self, assignment_type: str, assignment_id: int):
        self.assignment_type = assignment_type
        self.assignment_id = assignment_id

    def __str__(self):
        return f"('{self.assignment_id}', {self.assignment_type})"

    @staticmethod
    def get_assignment_type_list():
        minor = AssignmentType("Minor Assessment", 1)
        major = AssignmentType("Major Assessment", 2)
        return [minor, major]