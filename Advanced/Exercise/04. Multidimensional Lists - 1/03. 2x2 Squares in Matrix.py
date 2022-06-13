rows_number, columns_number = [int(i) for i in input().split(" ")]

matrix = []

for _ in range(rows_number):
    current = [i for i in input().split(" ")]
    matrix.append(current)

counter = 0

for row in range(rows_number - 1):
    for column in range(columns_number - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            counter += 1

print(counter)