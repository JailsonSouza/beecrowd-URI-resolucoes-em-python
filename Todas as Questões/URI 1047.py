hi,mi,hf,mf = input().split(" ")
hi = int(hi)
hf = int(hf)
mi = int(mi)
mf = int(mf)
hr = (24)
he = (0)
if ((hi > hf)and(mi == mf)):
  print('O JOGO DUROU',((hr - hi) + hf),'HORA(S) E',(he),'MINUTO(S)')
elif ((hi > hf)and(mi > mf)):
  print('O JOGO DUROU',(((hr - hi) + hf)-1),'HORA(S) E',((60 - mi) + mf),'MINUTO(S)')
elif ((hi > hf)and(mi < mf)):
  print('O JOGO DUROU',((hr - hi) + hf),'HORA(S) E',(mf-mi),'MINUTO(S)')
elif ((hi < hf)and(mi == mf)):
  print('O JOGO DUROU',(hf-hi),'HORA(S) E',(he),'MINUTO(S)')
elif ((hi < hf)and(mi > mf)):
  print('O JOGO DUROU',((hf-hi)-1),'HORA(S) E',((60 - mi) + mf),'MINUTO(S)')
elif ((hi < hf)and(mi < mf)):
  print('O JOGO DUROU',(hf-hi),'HORA(S) E',(mf-mi),'MINUTO(S)')
elif ((hi == hf)and(mi == mf)):
  print('O JOGO DUROU',(hr),'HORA(S) E',(he),'MINUTO(S)')
elif ((hi == hf)and(mi > mf)):
  print('O JOGO DUROU',((hr)-1),'HORA(S) E',((60 - mi) + mf),'MINUTO(S)')
elif ((hi == hf)and(mi < mf)):
  print('O JOGO DUROU 0 HORA(S) E',(mf-mi),'MINUTO(S)')