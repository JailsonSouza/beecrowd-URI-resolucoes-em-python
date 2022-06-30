i = 1
j = 3
rest = j
while i <= 9:
  j = rest + 4
  aux = 1
  while(aux <= 3):
    print('I={} J={}'.format(i,j))
    rest = (j)
    j -=1
    aux += 1
  i +=2