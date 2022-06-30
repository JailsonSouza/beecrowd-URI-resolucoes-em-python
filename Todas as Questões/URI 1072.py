cont = 1
de = 0
fo = 0
n = int(input())
while cont <= n:
  val = int(input())
  if((val >= 10)and(val <=20)):
    de += 1
  else:
    fo += 1
  cont += 1
print(de,'in')
print(fo,'out')