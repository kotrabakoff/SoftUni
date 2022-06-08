box_clothes = input().split()

box_clothes = [int(x) for x in box_clothes]

rack_capacity = int(input())
current_rack = rack_capacity
counter = 1

while len(box_clothes) > 0:
    index = 1
    for _ in range(len(box_clothes)):
        if current_rack < box_clothes[-index]:
            counter += 1
            current_rack = rack_capacity

        if box_clothes[-index] <= current_rack:
            current_rack -= box_clothes[-index]
            box_clothes.pop()
        else:
            index += 1
            continue

print(counter)
