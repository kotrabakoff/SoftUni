
n = int(input())

matrix = []

primary = []
secondary = []

reverse_index = n-1

for j in range(n):
    matrix.append([int(i) for i in input().split(" ")])
    primary.append(matrix[j][j])
    secondary.append(matrix[j][reverse_index])
    reverse_index -= 1

total_primary = sum(primary)
total_secondary = sum(secondary)

total = abs(total_primary - total_secondary)

print(total)
