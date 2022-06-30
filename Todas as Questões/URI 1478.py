while True:
  n = int(input())

  if n == 0:
    break

  M = []

  for l in range(1, n+1):
    L = []
    cont = l
    for c in range(n):
      L.append(abs(cont))
      if cont == 1:
        cont -= 3
      else:
        cont -= 1
    M.append(L)

  for i in range(n):
    tx = ''
    for j in range(n):
      tx += " %3d" %M[i][j]
    print(tx[1:])
  print('')