def Calculator(action, a, b):
    if action == "multiply":
        result = a * b
        return result
    elif action == "divide":
        result = int(a / b)
        return result
    elif action == "add":
        result = a + b
        return result
    elif action == "subtract":
        result = a - b
        return result

current_action = input()
current_a = int(input())
current_b = int(input())

print(Calculator(current_action, current_a, current_b))