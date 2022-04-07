projection = input()
row = int(input())
columns = int(input())

ticket = 0

if projection == "Premiere":
    ticket = 12
elif projection == "Normal":
    ticket = 7.5
else:
    ticket = 5

ticket *= row * columns

print(f"{ticket:.2f} leva")