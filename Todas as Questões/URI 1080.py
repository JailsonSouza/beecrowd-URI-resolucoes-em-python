for cont in range(1,101):
  x = int(input())
  if (cont == 1):
    maior = x
    pos = cont
  if (x > maior):
    maior = x
    pos = cont
print(maior)
print(pos)