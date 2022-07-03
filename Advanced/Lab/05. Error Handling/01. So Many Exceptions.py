
for i in range(3):
    numbers_list = [int(i) for i in input().split(", ")]
    result = 1
    for number in numbers_list:
        if number <= 5:
            result *= number
        elif number > 5 and number <= 10:
            result /= number
    print(f"{int(result)}")