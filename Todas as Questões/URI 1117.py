nv = 0
no = 0
while nv <= 2:
  n = float(input())
  if (n < 0) or (n > 10):
    print('nota invalida')
  else:
    no += n
    nv += 1
    if (nv == 2):
      print('media = {:.2f}'.format(no/2))