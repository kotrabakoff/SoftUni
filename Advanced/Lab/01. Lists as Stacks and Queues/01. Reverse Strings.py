initial = input()

initial_list = [char for char in initial]

stack = []

for _ in range(0, len(initial_list)):
    stack.append(initial_list.pop())

print(f"{''.join(stack)}")