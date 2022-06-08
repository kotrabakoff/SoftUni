lines = int(input())

stack = []

for i in range(0, lines):
    command = input()
    current = command.split()
    if current[0] == "1":
        stack.append(int(current[1]))
    elif current[0] == "2":
        if len(stack) > 0:
            stack.pop()
        else:
            continue
    elif current[0] == "3":
        print(f"{max(stack)}")
    elif current[0] == "4":
        print(f"{min(stack)}")
final = []

for x in range(len(stack)):
    final.append(str(stack.pop()))

print(f"{', '.join(final)}")

