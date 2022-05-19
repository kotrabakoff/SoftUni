factor = int(input())
count = int(input())
list = []
element = int(factor)

for i in range(count):
    list.append(element)
    element += factor

print(list)