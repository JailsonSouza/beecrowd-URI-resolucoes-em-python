c = 1
n = int(input())
while c <= n:
  si = 0
  x,y = input().split(" ")
  x = int(x)
  y = int(y)
  if (x > y):
    y = y + 1
    x = x - 1
    while y <= x:
      if (y % 2 != 0):
        si = si + y
      y += 1 
    print(si)
  elif (x < y):
    x = x + 1
    y = y - 1
    while x <= y:
      if (x % 2 != 0):
        si = si + x
      x += 1
    print(si)
  else:
    print('0')
  c += 1