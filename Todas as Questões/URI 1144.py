n = int(input())
n1 = 1
for i in range(1, n+1):
  print('{} {} {}'.format(n1,n1**2,n1**3))
  print('{} {} {}'.format(n1,(n1**2)+1,(n1**3)+1))
  n1 += 1