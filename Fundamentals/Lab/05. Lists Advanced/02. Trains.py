wagons = int(input())

train = [0 for i in range(0, wagons)]
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    place = command[1]

    if action == "add":
        train[-1] += int(command[1])

    elif action == "insert":
        train[int(place)] += int(command[2])

    elif action == "leave":
        train[int(place)] -= int(command[2])
    command = input()
print(train)