rooms = int(input())
room_Number = 1
frees = 0
deficit = False
for i in range(rooms):
    current_Room = input().split(" ")
    chairs = len(current_Room[0])
    people = int(current_Room[1])
    if chairs < people:
        print(f"{people - chairs} more chairs needed in room {room_Number}")
        deficit = True
    else:
        frees += (chairs - people)
    room_Number += 1

if frees >= 0 and deficit == False:
    print(f"Game On, {frees} free chairs left")