rows = int(input())

final_list = []

for _ in range(rows):
    current = [int(i) for i in input().split(", ")]
    for i in current:
        final_list.append(i)

print(final_list)