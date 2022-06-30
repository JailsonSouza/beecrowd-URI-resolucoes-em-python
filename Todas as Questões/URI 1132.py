soma = 0
n = int(input())
m = int(input())
if (n < m):
  for i in range(n, m+1):
    if (i % 13 != 0):
      soma += i
elif (n > m):
  for i in range(m, n+1):
    if (i % 13 != 0):
      soma += i
print(soma)