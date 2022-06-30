vetor = []
for c in range(0,10):
  n = int(input())
  if n <= 0:
    vetor.append(1)
  else:
    vetor.append(n)
for c, i in enumerate(vetor):
  print('X[{}] = {}'.format(c, vetor[c]))