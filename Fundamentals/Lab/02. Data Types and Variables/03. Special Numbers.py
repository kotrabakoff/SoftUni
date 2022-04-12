number = int(input())

for i in range(1, number + 1):
    digits = i
    final = 0
    while digits > 0:
        final += digits % 10
        digits = int(digits / 10)

    is_special = final == 5 or final == 7 or final == 11
    print(f"{i} -> {is_special}")


