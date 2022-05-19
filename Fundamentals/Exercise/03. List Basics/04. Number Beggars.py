n = list(map(int, (input().split(", "))))
beggars = int(input())
start = 0
final = []

for i in range(0, beggars):
    final.append(sum(n[start::beggars]))
    start += 1


print(final)