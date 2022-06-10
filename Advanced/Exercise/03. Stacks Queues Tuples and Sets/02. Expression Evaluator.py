from collections import deque

initial = input().split(" ")

operands = ["-", "+", "*", "/"]

operations = {
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}

working_deque = deque()

total = []

for i in initial:
    if i in operands:
        while len(working_deque) > 1:
            left = working_deque.popleft()
            right = working_deque.popleft()
            result = operations[i](left, right)
            working_deque.appendleft(result)
    else:
        working_deque.append(int(i))



print(working_deque.popleft())