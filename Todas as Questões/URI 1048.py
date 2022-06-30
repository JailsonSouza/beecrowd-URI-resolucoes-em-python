s = float(input())
if((s >= 0)and(s <= 400)):
  p = 15
elif((s > 400)and(s <= 800)):
  p = 12
elif((s > 800)and(s <= 1200)):
  p = 10
elif((s > 1200)and(s <= 2000)):
  p = 7
elif(s > 2000):
  p = 4
b = ((s * p)/100)
st = (s+b)
print('Novo salario: {:.2f}'.format(st))
print('Reajuste ganho: {:.2f}'.format(b))
print('Em percentual: {} %'.format(p))