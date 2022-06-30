import math
a,b,c = input().split(" ")
a, b, c = float(a), float(b), float(c)
delt = ((b*b)-4*a*c)
if((a == 0) or (delt < 0)):
  print('Impossivel calcular')
else:
  raiz = math.pow(delt,1/2)
  r1 = (((-b) + raiz)/(2*a))
  r2 = (((-b) - raiz)/(2*a))
  print('R1 = {:.5f}'.format(r1))
  print('R2 = {:.5f}'.format(r2))