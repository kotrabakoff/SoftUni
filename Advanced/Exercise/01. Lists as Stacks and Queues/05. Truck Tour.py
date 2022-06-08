from collections import deque
pumps_number = int(input())

round = deque()

for _ in range(pumps_number):
    round.append([int(x) for x in input().split()])

possible = False

current_try = round
counter = 0

for _ in range(pumps_number):
    current_petrol = 0
    for petrol, distance in current_try:
        current_petrol += petrol
        if current_petrol >= distance:
            current_petrol -= distance
            possible = True
            continue
        else:
            possible = False
            break
    if possible == True:
        break
    counter += 1
    current_try.append(round.popleft())

print(counter)