class Room:
    def __init__(self,room):
        self.room=room
        #id auto increments

    def __str__(self):
        return "INSERT INTO Room VALUES (null, \""+self.room+"\");"

roomList = []
roomDict = {}
roomID=1
for i in range(1,21):
    for char in "NWSE":
        for j in range (0, 9):
            if j==0:
                rom="B"+char+str(i)
                room=Room(rom)
                roomList.append(room)
            else:
                rom = str(j) + char + str(i)
                room = Room(rom)
                roomList.append(room)
            roomDict[roomID]="Unoccupied "+rom
            roomID+=1

print(roomDict.items())
for room in roomList:
    with open('cmd.sql','a') as f:
        print(room.__str__(),file = f)