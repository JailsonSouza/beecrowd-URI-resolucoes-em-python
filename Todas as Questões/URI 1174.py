vetor = []

for c in range(0, 100):
  vetor.append(float(input()))

for c, i in enumerate(vetor):
  if vetor[c] <= 10:
    print('A[{}] = {}'.format(c, vetor[c]))