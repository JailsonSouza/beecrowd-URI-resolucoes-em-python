n = int(input())
for c in range(0,n):
    soma = 0
    cont = 1
    a,b = input().split()
    a = int(a)
    b = int(b)
    while cont <= b:
        if a % 2 != 0:
            soma += a
            cont += 1
        a += 1
    print(soma)
