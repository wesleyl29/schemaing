from course import Course


class Class:
    def __init__(self, period: int, room_id: int, teacher_id: int, course_id: int):
        self.period = period
        self.room_id = room_id
        self.teacher_id = teacher_id
        self.course_id = course_id

    def __str__(self):
        return f"INSERT INTO Class ( Period, RoomID, TeacherID, CourseID, ClassID ) VALUES ( {self.period}, {self.room_id}, {self.teacher_id}, {self.course_id} );"

    @staticmethod
    def get_dictionary():
        pass


course_dictionary = Course.get_dictionary()