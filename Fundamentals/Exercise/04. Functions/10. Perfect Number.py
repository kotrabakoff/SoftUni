def Perfect_Number(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i

    if a == sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

num = int(input())

Perfect_Number(num)