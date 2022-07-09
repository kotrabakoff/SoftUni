file = open("numbers.txt", 'r')

result = 0

for i in file:
    number = int(i)
    result += number

print(result)