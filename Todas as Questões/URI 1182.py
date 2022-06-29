M = []
coluna = int(input())
escolha = str(input())
tam = 12

for i in range(tam):
    L = []
    for j in range(tam):
        L.append(float(input()))
    M.append(L)
soma = 0
if escolha == 'S':
    for i in range(tam):
        soma += M[i][coluna]
    valor = soma
elif escolha == 'M':
    for i in range(tam):
        soma += M[i][coluna]
    valor = soma / tam

print('{:.1f}'.format(valor))