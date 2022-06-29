M = []
cont = 0
soma = 0
opcao = input()
for i in range(12):
    L = []
    for j in range(12):
        n = float(input())
        if (j + i) < 11:
            soma += n
            cont += 1
        L.append(n)
    M.append(L)
if opcao == 'S':
    print(f'{soma:.1f}')
elif opcao == 'M':
    media = soma / cont
    print(f'{media:.1f}')