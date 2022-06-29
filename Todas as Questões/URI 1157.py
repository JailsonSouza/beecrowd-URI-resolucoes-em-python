cont = 1
n = int(input())
while cont <= n:
    if n % cont == 0:
        print(cont)
    cont += 1