while True:
  n, m = input().split()
  n, m = int(n), int(m)
  if (n == 0) or (m == 0):
    break
  if (n > 0) and (m > 0):
    print('primeiro')
  elif (n < 0) and (m > 0):
    print('segundo')
  elif (n < 0) and (m < 0):
    print('terceiro')
  else:
    print('quarto')