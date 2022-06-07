import re

pattern = r"([U][$])([A-Z][a-z]{2,})(\1)([P][@][$])([A-Za-z]{5,}[0-9]+)(\4)"
iterations = int(input())
success = 0

for i in range(0, iterations):
    current = re.match(pattern, input())
    if current is not None:
        print(f"Registration was successful\nUsername: {current.group(2)}, Password: {current.group(5)}")
        success += 1

    elif current is None:
        print("Invalid username or password")


print(f"Successful registrations: {success}")