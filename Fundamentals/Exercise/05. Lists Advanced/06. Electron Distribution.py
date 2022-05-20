def Electrons(a):
    shell = 1
    separated = []
    while a > 0:
        electrons_In_Shell = 2*shell**2
        if a <= electrons_In_Shell:
            separated.append(a)
            break
        separated.append(electrons_In_Shell)
        shell += 1
        a -= electrons_In_Shell
        electrons_In_Shell = 0
    return separated

initial = int(input())

print(Electrons(initial))

