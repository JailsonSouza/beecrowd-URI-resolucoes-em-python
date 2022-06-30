vetor = []
n = int(input())
for c in range(0, 10):
  if c == 0:
    n = n
  else:
    n *= 2
  vetor.append(n)
for c, i in enumerate(vetor):
  print('N[{}] = {}'.format(c, vetor[c]))