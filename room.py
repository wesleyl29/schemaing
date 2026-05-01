class Room:
    def __init__(self,room,occupied):
        self.room=room
        self.occupied=False
        #id auto increments

    def __str__(self):
        return "INSERT INTO Room VALUES (null, \""+self.room+"\");"

    @staticmethod
    def get_dict() -> dict:
        dictionary = {}
        count = 1
        for i in range(1, 21):
            for char in "NWSE":
                for j in range(0, 9):
                    if j == 0:
                        rom = "B" + char + str(i)
                    else:
                        rom = str(j) + char + str(i)
                    dictionary[rom]=count

        return dictionary

roomList = []
roomID=1
for i in range(1,21):
    for char in "NWSE":
        for j in range (0, 9):
            if j==0:
                rom="B"+char+str(i)
                room=Room(rom,False)
                roomList.append(room)
            else:
                rom = str(j) + char + str(i)
                room = Room(rom,False)
                roomList.append(room)

print(Room.get_dict())
for room in roomList:
    with open('cmd.sql','a') as f:
        print(room.__str__(),file = f)