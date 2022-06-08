initial = input().split()

stack_final = []

stack_final = [initial.pop() for x in range(len(initial))]

# for i in range(len(initial)):
#     stack_final.append(initial.pop())

print(f"{' '.join(stack_final)}")