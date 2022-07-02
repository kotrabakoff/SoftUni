n = int(input())
matrix = []

for _ in range(n):
    current = [i for i in input()]
    matrix.append(current)

symbol = input()

occurrence = []

iteration = 0

for row in matrix:
    iterations_columns = 0
    for column in row:
        if symbol in column:
            occurrence.append(iteration)
            occurrence.append(iterations_columns)
        iterations_columns += 1
    iteration += 1

occurrence = tuple(occurrence)

if occurrence:
    print(occurrence)
else:
    print(f"{symbol} does not occur in the matrix")