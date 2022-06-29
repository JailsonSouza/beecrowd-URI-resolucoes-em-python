n = int(input())
a = input()
a = a.split()
for c in range(len(a)):
    a[c] = int(a[c])
menor = a[0]
posicao = 0

for j in range(1, len(a)):
    if a[j] < menor:
        menor = a[j]
        posicao = j
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))