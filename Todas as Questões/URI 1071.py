soma = 0
x = int(input())
y = int(input())
if(x > y):
  aux = y
  while aux <= x:
    if (aux == y):
      x = x - 1
      aux = aux + 1
    if(aux % 2 != 0):
      soma += (aux)
    aux +=1
  print(soma)
elif(x < y):
  aux = x
  while aux <= y:
    if (aux == x):
        y = y - 1
        aux = aux + 1
    if(aux % 2 != 0):
        soma += (aux)
    aux +=1
  print(soma)
else:
  print(soma)