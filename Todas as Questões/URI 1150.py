x = int(input())
z = -9999999
while z <= x:
  z = int(input())
soma = x
total = 1
while soma < z:
  soma += x + total
  total += 1
print(total)