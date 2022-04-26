def Min_Max_Sum(a):
    print(f"The minimum number is {min(a)}")
    print(f"The maximum number is {max(a)}")
    print(f"The sum number is: {sum(a)}")

console = list(map(int, input().split()))

Min_Max_Sum(console)