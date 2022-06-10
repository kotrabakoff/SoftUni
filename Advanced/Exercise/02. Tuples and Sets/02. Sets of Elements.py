n_m = input().split()

n = int(n_m[0])
m = int(n_m[1])

set_n = set()
set_m = set()

for i in range(n):
    number_n = input()
    set_n.add(number_n)

for j in range(m):
    number_m = input()
    set_m.add(number_m)

final = []

for k in set_n:
    if k in set_m:
        final.append(k)

for l in final:
    print(l)