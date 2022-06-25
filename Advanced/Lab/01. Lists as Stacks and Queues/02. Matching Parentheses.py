initial = input()

stack = []

for i in range(len(initial)):
    ch = initial[i]
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        start_index = stack.pop()
        end_index = i + 1
        print(initial[start_index:end_index])


