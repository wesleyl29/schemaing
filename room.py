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
                    count+=1
        return dictionary

room_list = []
for i in range(1,21):
    for char in "NWSE":
        for j in range (0, 9):
            if j==0:
                rom="B"+char+str(i)
                room=Room(rom,False)
                room_list.append(room)
            else:
                rom = str(j) + char + str(i)
                room = Room(rom,False)
                room_list.append(room)

print(Room.get_dict())
with open('cmd.sql','a') as f:
    for room in room_list:
        print(room.__str__(),file = f)