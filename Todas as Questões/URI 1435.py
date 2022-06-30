while True:
  n = int(input())
  if n == 0:
    break
  M = []
  for l in range(n):
    L = []
    for c in range(n):
      L.append(1)
    M.append(L)

  valor = 1
  cima = 0
  esq = 0
  baixo = n - 1
  direita = n - 1

  if (n % 2 == 0):
    meio = n / 2

  else:
    meio = (n + 1) / 2

  while valor <= meio:
    i = esq
    while i <= direita:
      M[cima][i] = valor
      M[baixo][i] = valor
      i+=1

    i = (cima + 1)
    while i < baixo:
      M[i][esq] = valor
      M[i][direita] = valor
      i += 1

    valor += 1
    cima += 1
    baixo -= 1
    esq += 1
    direita -= 1

  for i in range(n):
    tx = ''
    for j in range(n):
      tx += " %3d" %M[i][j]
    print(tx[1:])
  print('')