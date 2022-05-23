import string
initial = input().split(", ")
final = []
flag = 0
exceptions = string.ascii_letters + string.digits + "_" + "-"
expected_elements = []

for i in initial:
    expected_elements = []
    flag = 0
    if len(i) < 3 or len(i) > 16:
        flag = 1
    for j in i:
        if j in exceptions:
            expected_elements.append(j)
    if len(expected_elements) != len(i):
        flag = 1
    if flag == 0:
        print(i)
