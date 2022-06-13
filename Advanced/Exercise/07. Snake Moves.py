from collections import deque

rows, columns = [int(i) for i in input().split(" ")]

counter = 0
word = input()

for i in range(rows):
    elements = [None] * columns
    if i % 2 == 0:
        for j in range(columns):
            elements[j] = word[counter % len(word)]
            counter += 1
    else:
        for k in range(columns - 1, - 1, -1):
            elements[k] = word[counter % len(word)]
            counter += 1
    print(''.join(elements))

# a = 10 % len("softuni")
#
# print(a)