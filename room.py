class Room:
    def __init__(self,room):
        self.room=room
        #id auto increments

    def __str__(self):
        return "INSERT INTO Room VALUES (null, \""+self.room+"\");"

roomList = []

for i in range(1,21):
    for char in "NWSE":
        rom="B"+char+str(i)
        room=Room(rom)
        roomList.append(room)
        for j in range (1, 9):
            rom=str(j)+char+str(i)
            room = Room(rom)
            roomList.append(room)

for room in roomList:
    with open('cmd.sql','a') as f:
        print(room.__str__(),file = f)