t = int(input())
for i in range(t):
  soma = 0
  n = int(input())
  for c in range(1, n+1):
    if n % c == 0:
      soma += c
  if soma == n+1:
    print('{} eh primo'.format(n))
  else:
    print('{} nao eh primo'.format(n))