vetor = []
n = float(input())
for c in range(0, 100):
    vetor.append(n)
    n /= 2
for j, i in enumerate(vetor):
    print('N[{}] = {:.4f}'.format(j, vetor[j]))