
try:
    text = input()
    recurrs = int(input())
    print(text*recurrs)

except ValueError:
    print("Variable times must be an integer")
