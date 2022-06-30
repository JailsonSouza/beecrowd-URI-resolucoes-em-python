while True:
  n,m = input().split()
  n, m = int(n), int(m)
  menor = min(m,n)
  maior = max(m,n)
  if (menor <= 0) or (maior <= 0):
    break
  lista = ""
  soma = 0
  for i in range(menor, maior+1):
    soma += i
    lista += str(i) + " "
  print("{}Sum={}".format(lista, soma))