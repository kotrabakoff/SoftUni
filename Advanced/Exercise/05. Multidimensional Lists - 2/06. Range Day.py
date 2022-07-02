size = 5

shooting_range = []

for i in range(size):
    current_row = input().split()
    for j in range(size):
        if current_row[j] == "A":
            start_row = i
            start_col = j
    shooting_range.append(current_row)

directions = {
    "up": lambda x, y: (x-1, y),
    "down": lambda x, y: (x+1, y),
    "left": lambda x, y: (x, y-1),
    "right": lambda x, y: (x, y+1)
}

commands_number = int(input())
row = start_row
col = start_col

target_shot = []

counter = 0

check = False

for i in range(commands_number):
    counter = 0
    for k in shooting_range:
        if "x" not in k:
            pass
        else:
            counter += 1
    if counter <= 0:
        print(f"Training completed! All {len(target_shot)} targets hit.")
        break
    current_command = input().split()
    action = current_command[0]
    direction = current_command[1]
    if action == "shoot":
        shoot_row = row
        shoot_col = col
        shoot_row, shoot_col = directions[direction](row, col)
        while 0 <= shoot_row < size and 0 <= shoot_col < size:
            if shooting_range[shoot_row][shoot_col] == ".":
                shoot_row, shoot_col = directions[direction](shoot_row, shoot_col)
                continue
            if shooting_range[shoot_row][shoot_col] == "x":
                shooting_range[shoot_row].pop(shoot_col)
                shooting_range[shoot_row].insert(shoot_col, ".")
                target_shot.append([shoot_row, shoot_col])
                continue
    elif action == "move":
        steps = int(current_command[2])
        previous_row = row
        previous_col = col
        for j in range(steps):
            next_row, next_col = directions[direction](row, col)
            if 0 <= next_row < size and 0 <= next_col < size:
                next_row, next_col = directions[direction](row, col)
            else:
                check = True
                break
            if 0 <= row < size and 0 <= col < size and shooting_range[next_row][next_col] == ".":
                row, col = directions[direction](row, col)
        shooting_range[previous_row].pop(previous_col)
        shooting_range[previous_row].insert(previous_col, ".")
        shooting_range[row].pop(col)
        shooting_range[row].insert(col, "A")

    counter = 0
    for k in shooting_range:
        if "x" not in k:
            pass
        else:
            counter += 1
    if counter <= 0:
        print(f"Training completed! All {len(target_shot)} targets hit.")
        break

if counter > 0:
    print(f"Training not completed! {counter} targets left.")

print(*target_shot, sep='\n')
