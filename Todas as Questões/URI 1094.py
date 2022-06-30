n = int(input())
cont = 1
total = 0
tc = 0
tr = 0
ts = 0
while cont <= n:
  quant,tip = input().split(" ")
  quant = int(quant)
  tip = str(tip)
  total = total + quant
  if (tip == 'C'):
    tc = tc + quant
  elif(tip == 'R'):
    tr = tr + quant
  elif(tip == 'S'):
    ts = ts + quant
  cont += 1
pc = ((tc*100)/total)
pr = ((tr*100)/total)
ps = ((ts*100)/total)
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(tc))
print('Total de ratos: {}'.format(tr))
print('Total de sapos: {}'.format(ts))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))