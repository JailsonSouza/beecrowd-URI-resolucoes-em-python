valores = input().split()
a = int(valores[0])
ult = len(valores) -1
n = int(valores[ult])
soma = 0
for c in range(0,n):
  soma += a + c
print(soma)