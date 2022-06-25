repeats = int(input())

number = ["1","2","3""4","5","6","7","8","9","0"]

regulars = set()
vips = set()

for i in range(repeats):
    guest = input()
    if guest[0] in number:
        vips.add(guest)
    else:
        regulars.add(guest)

visitor = input()

while visitor != "END":
    if visitor in regulars:
        regulars.remove(visitor)

    if visitor in vips:
        vips.remove(visitor)
    visitor = input()

regulars = sorted(regulars)
vips = sorted(vips)

print(f"{len(vips) + len(regulars)}")

for vip in vips:
    print(vip)

for regular in regulars:
    print(regular)
