class Room:
    room_dict = {}

    def __init__(self, room: str, room_id: int):
        self.room = room
        self.room_id = room_id
        Room.room_dict[room] = room_id

    def __str__(self):
        return f"INSERT INTO Room (Class) VALUES ('{self.room}');"

    @property
    def get_id(self):
        return self.room_id

    @staticmethod
    def get_room_list() -> list:
        room_list = []
        count = 1
        for i in range(1,21):
            for char in "NWSE":
                for j in range (0, 9):
                    if j == 0:
                        rom = "B"+ char + str(i)
                        room = Room(rom, count)
                        count += 1
                        room_list.append(room)
                    else:
                        rom = str(j) + char + str(i)
                        room = Room(rom, count)
                        count += 1
                        room_list.append(room)
        return room_list
    

