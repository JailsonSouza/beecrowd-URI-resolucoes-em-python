vetor = []
n = int(input())
for c in range(0, 999):
  for t in range(0, n):
    if len(vetor) <= 999:
      vetor.append(t)
    else:
      break
for j, i in enumerate(vetor):
  print('N[{}] = {}'.format(j, vetor[j]))