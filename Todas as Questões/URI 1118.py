resp = 1
while resp != 2:
  resp = 1
  aux = 1
  soma = 0
  while (aux <= 2) and (resp == 1):
    n = float(input())
    if (n < 0) or (n > 10):
      print('nota invalida')
    else:
      aux += 1
      soma += n
  print('media = {:.2f}'.format(soma/2))
  resp = 4
  while (resp != 1) and (resp != 2):
    resp = int(input('novo calculo (1-sim 2-nao)\n'))