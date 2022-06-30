i = 0
while i < 2.1:
  j = 1
  while j <= 3:
    k = i + j
    if ((i == 0)or(i == 1)or((i > 1.9)and(i < 2.1))):
      print('I={:.0f} J={:.0f}'.format(i,k))
    else:
      print('I={:.1f} J={:.1f}'.format(i,k))
    j += 1
  i += 0.2