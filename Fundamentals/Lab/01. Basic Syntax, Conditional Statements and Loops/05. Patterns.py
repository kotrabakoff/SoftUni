stars = int(input())

starasc = stars

for i in range(starasc + 1):
    print(i * "*")
    starasc += 1

for j in range(stars - 1, 0, -1):
    print(j * "*")
    stars -= 1
