from collections import deque

quantity = int(input())
name = input()
list = deque()

while name != "Start":
    list.appendleft(name)
    name = input()

command = input()

while command != "End":
    current = command.split()
    if current[0] == "refill":
        quantity += int(current[1])
    else:
        litres = int(command)
        if litres <= quantity:
            print(f"{list[-1]} got water")
            list.pop()
            quantity -= litres
        else:
            print(f"{list[-1]} must wait")
            list.pop()
    command = input()

print(f"{quantity} liters left")