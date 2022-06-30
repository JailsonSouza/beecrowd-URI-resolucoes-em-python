impar = []
par = []
for c in range(0, 15):
  n = int(input())
  if n % 2 == 0:
    par.append(n)
  else:
    impar.append(n)
  if len(impar) == 5:
    for j, i in enumerate(impar):
      print('impar[{}] = {}'.format(j, impar[j]))
    impar.clear()
  if len(par) == 5:
    for j, i in enumerate(par):
      print('par[{}] = {}'.format(j, par[j]))
    par.clear()
for j, i in enumerate(impar):
  print('impar[{}] = {}'.format(j, impar[j]))
for j, i in enumerate(par):
  print('par[{}] = {}'.format(j, par[j]))