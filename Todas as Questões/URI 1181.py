matriz = []
linha = int(input())
escolha = str(input())
tam = 12

for i in range(tam):
    linha_m = []
    for j in range(tam):
        linha_m.append(float(input()))
    matriz.append(linha_m)
if escolha == 'S':
    soma = 0
    for z in matriz[linha]:
        soma += z
    valor = soma
elif escolha == 'M':
    soma = 0
    for z in matriz[linha]:
        soma += z
    valor = soma / tam

print(f'{valor:.1f}')