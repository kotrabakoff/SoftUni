repeats = int(input())
list = []

for i in range(0, repeats):
    number = int(input())
    list.append(number)

command = input()

new_list = []

if command == "even":
    new_list = [j for j in (list) if j % 2 == 0]

if command == "odd":
    new_list = [j for j in (list) if j % 2 == 1]

if command == "positive":
    new_list = [j for j in (list) if j >= 0]

if command == "negative":
    new_list = [j for j in (list) if j < 0]


print(new_list)