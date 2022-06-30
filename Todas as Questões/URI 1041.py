n1, n2 = input().split(" ")
n1, n2 = float(n1), float(n2)
if((n1 == 0) and (n2 == 0)):
  print('Origem')
elif((n1 > 0) and (n2 > 0)):
  print('Q1')
elif((n1 < 0) and (n2 > 0)):
  print('Q2')
elif((n1 < 0) and (n2 < 0)):
  print('Q3')
elif((n1 > 0) and (n2 < 0)):
  print('Q4')
elif((n1 == 0) and ((n2 > 0) or (n2 < 0))):
  print('Eixo Y')
elif(((n1 > 0) or (n1 < 0)) and (n2 == 0)):
  print('Eixo X')