first = set(input().split(" "))

second = set(input().split(" "))

n = int(input())

for i in range(n):
    initial = input()
    line = initial.split()
    if initial == "Check Subset":
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")
        continue
    line = initial.split()
    command = line[0]
    set_number = line[1]
    current = set(line[2:])
    if command == "Add":
        if set_number == "First":
            first = first | current
        elif set_number == "Second":
            second = second | current
    elif command == "Remove":
        if set_number == "First":
            first -= current
        elif set_number == "Second":
            second -= current

first = sorted(first)
second = sorted(second)

print(*first, sep=", ")
print(*second, sep=", ")

