n1 = int(input())
n2 = int(input())
operator = input()

result = 0
eo = None

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        eo = "even"
    else:
        eo = "odd"
    print(f"{n1} {operator} {n2} = {result} - {eo}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        eo = "even"
    else:
        eo = "odd"
    print(f"{n1} {operator} {n2} = {result} - {eo}")

elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        eo = "even"
    else:
        eo = "odd"
    print(f"{n1} {operator} {n2} = {result} - {eo}")

elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")

else:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")
