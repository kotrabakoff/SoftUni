n = int(input())
word = input()
list = []
filter = []


for i in range(0, n):
    string = (input())
    list.append(string)
    if word in string:
        filter.append(string)

print(list)
print(filter)