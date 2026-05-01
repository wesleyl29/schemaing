class AssignmentType:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def get_dict() -> dict:
        dictionary = {}
        dictionary["Minor Assessment"] = 1
        dictionary["Major Assessment"] = 2
        return dictionary

with open('cmd.sql','a') as f:
    print("INSERT INTO AssignmentType VALUES (1, Minor Assessment);", file = f)
    print("INSERT INTO AssignmentType VALUES (2, Major Assessment);", file = f)