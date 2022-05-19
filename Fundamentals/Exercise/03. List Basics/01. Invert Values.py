string = input().split(" ")
new_list = []


for i in string:
    if int(i) >= 0:
        new_list.append(-int(i))
    else:
        new_list.append(abs(int(i)))

print(new_list)