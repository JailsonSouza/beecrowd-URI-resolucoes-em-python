t = int(input())
for i in range(t):
  soma = 0
  n = int(input())
  for c in range(1, n-1):
    if n % c == 0:
      soma += c
  if soma == n:
    print('{} eh perfeito'.format(n))
  else:
    print('{} nao eh perfeito'.format(n))