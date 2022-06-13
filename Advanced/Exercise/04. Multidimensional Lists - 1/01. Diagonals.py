n = int(input())

matrix = []
index = 0
index_reverse = -1
primary = []
secondary = []

for _ in range(n):
    current_row = [int(i) for i in input().split(", ")]
    matrix.append(current_row)
    primary.append(matrix[index][index])
    secondary.append(matrix[index][index_reverse])
    index += 1
    index_reverse -= 1

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(f"Primary diagonal: {', '.join([str(k) for k in primary])}. Sum: {primary_sum}")

print(f"Secondary diagonal: {', '.join([str(k) for k in secondary])}. Sum: {secondary_sum}")