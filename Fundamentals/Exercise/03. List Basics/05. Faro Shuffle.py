list = input().split(" ")
shuffles = int(input())
pos_index = 0
neg_index = -int(len(list) / 2)
half = int(len(list) / 2)

for i in range(shuffles):
    new_list = []
    for j in range(half):
        new_list.append(list[pos_index])
        new_list.append(list[neg_index])
        pos_index += 1
        neg_index += 1
    list = new_list
    pos_index = 0
    neg_index = -int(len(list) / 2)

print(new_list)
