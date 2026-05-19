class Room:
    increasing_room_id = 1

    def __init__(self, room: str, room_id: int):
        self.room = room
        self.room_id = room_id

    def __str__(self):
        return f"INSERT INTO Room (Class) VALUES ('{self.room}');"

    @staticmethod
    def room_cmds() -> list:
        room_list = []
        for i in range(1,21):
            for char in "NWSE":
                for j in range (0, 9):
                    if j == 0:
                        rom = "B"+ char + str(i)
                        room = Room(rom, Room.increasing_room_id)
                        Room.increasing_room_id+=1
                        room_list.append(room)
                    else:
                        rom = str(j) + char + str(i)
                        room = Room(rom, Room.increasing_room_id)
                        Room.increasing_room_id+=1
                        room_list.append(room)
        return room_list
