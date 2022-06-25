n, m = [int(i) for i in input().split(", ")]

final = 0
matrix = []

for _ in range(n):
    current = [int(j) for j in input().split(", ")]
    matrix.append(current)
    final += sum(current)

print(final)
print(matrix)