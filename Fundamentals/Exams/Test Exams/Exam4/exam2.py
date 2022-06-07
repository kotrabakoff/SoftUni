import re

pattern = r"([U][$])([A-Z][a-z]{2,})(\1)([P][@][$])([A-Za-z]{5,}[0-9]+)(\4)"
iterations = int(input())
success = 0

for i in range(0, iterations):
    registration = input()
    if re.finditer(pattern, registration) is not None:
        for j in re.finditer(pattern, registration):
            print(f"Registration was successful\nUsername: {j.group(2)}, Password: {j.group(5)}")
        if success > 1:
            print(j.group)
        success += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {success}")


# import re
#
# pattern = r"([U][$])([A-Z][a-z]{2,})(\1)([P][@][$])([A-Za-z]{5,}[0-9]+)(\4)"
# iterations = int(input())
# success = 0
#
# for i in range(0, iterations):
#     current = re.finditer(pattern, input())
#     if current is not None:
#         for j in current:
#             print(f"Registration was successful\nUsername: {j.group(2)}, Password: {j.group(5)}")
#             success += 1
#     elif j is not None:
#         print("Invalid username or password")
#
#
# print(f"Successful registrations: {success}")