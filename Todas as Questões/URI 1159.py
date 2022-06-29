while True:
    num = int(input())
    if num == 0:
        break
    cont = 1
    soma = 0
    while cont <= 5:
        if num % 2 == 0:
            soma += num
            cont += 1
        num += 1
    print(soma)