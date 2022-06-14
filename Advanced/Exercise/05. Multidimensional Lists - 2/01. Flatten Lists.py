initial = input().split("|")

current_list = []

for i in range(len(initial)):
    current = initial.pop().split()
    for j in current:
        if j != " ":
            current_list.append(j)
print(' '.join(current_list), sep=" ")