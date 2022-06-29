vetor = []
for c in range(0, 20):
    vetor.append(int(input()))
for c in range(0, 10):
    aux = vetor[c]
    vetor[c] = vetor[19 - c]
    vetor[19 - c] = aux
for c, i in enumerate(vetor):
  print('N[{}] = {}'.format(c, vetor[c]))