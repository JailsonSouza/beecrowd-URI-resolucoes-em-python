a, b = input().split(" ")
a, b = int(a), int(b)
if (a == 1):
  tot = (4*b)
elif (a == 2):
  tot = (4.50*b)
elif (a == 3):
  tot = (5*b)
elif (a == 4):
  tot = (2*b)
elif (a == 5):
  tot = (1.50*b)
print('Total: R$ {:.2f}'.format(tot))