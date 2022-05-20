def Even_lenght(a):
    final = []
    for i in a:
        if len(i) % 2 == 0:
            final.append(i)
    final = "\n".join(final)
    return(final)

initial = input().split(" ")

print(Even_lenght(initial))