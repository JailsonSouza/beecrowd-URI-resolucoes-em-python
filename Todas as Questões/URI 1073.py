cont = 2
n = int(input())
while cont <= n:
  if cont % 2 == 0:
    resp = (cont **2)
    print('{}^2 = {}'.format(cont,resp))
  cont +=2