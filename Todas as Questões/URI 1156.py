s = 0
j = i = 1
while i <= 39:
  s += (i / j)
  j += j
  i += 2
print('{:.2f}'.format(s))