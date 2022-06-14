rows = int(input())

matrix = []

for i in range(rows):
    line_input = [int(j) for j in input().split()]
    matrix.append(line_input)

command = input()

while command != "END":
    command = command.split()
    action = command[0]
    row = int(command[1])
    column = int(command[2])
    new_value = int(command[3])
    if 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
        if action == "Add":
            new_value = new_value + matrix[row][column]
            matrix[row][column] = new_value
        elif action == "Subtract":
            new_value = matrix[row][column] - new_value
            matrix[row][column] = new_value


    else:
        print("Invalid coordinates")
    command = input()

for i in matrix:
    print(' '.join([str(j) for j in i]))