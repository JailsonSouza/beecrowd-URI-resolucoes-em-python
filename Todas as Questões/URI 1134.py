a = 0
g = 0
d = 0
n = 0
while n != 4:
  n = int(input())
  if(n == 1):
    a += 1
  elif(n == 2):
    g += 1
  elif(n == 3):
    d += 1
print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))