rows = int(input())

matrix = []

for i in range(rows):
    # current = [int(j) for j in input().split(", ")]
    matrix.append([k for k in [int(j) for j in input().split(", ")] if k % 2 == 0])

print(matrix)